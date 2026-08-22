# Purpose: Adapt Gazebo ROS 2 topics and coordinates to the AutomobileData contract.
# Inputs: Simulator localisation, IMU, camera, encoder odometry, sonar, and feedback topics.
# Outputs: Normalised graph-frame vehicle state and JSON simulator command messages.


"""ROS 2 adapter for Simulator_UniPD-DriveOps."""

import json
import math
from collections import deque

import numpy as np
from cv_bridge import CvBridge
from nav_msgs.msg import Odometry
from rclpy.node import Node
from sensor_msgs.msg import Image, Imu, LaserScan
from std_msgs.msg import Bool, Float32, String

from brain_core.vehicle_interface.automobile_data import Automobile_Data
from brain_interfaces.msg import Conditions, Localisation


# Gazebo lays the track texture over a 14.68 m x 14.99 m plane whose origin is
# at x=0 and whose y coordinate is exposed by the GPS plugin as abs(world_y).
# The brain graph was authored against the 5338 x 3541 map image at
# 3541 pixels / 15 metres.  Consequently its horizontal metric extent is
# wider than Gazebo's plane, and the two axes need independent scale factors.
GAZEBO_TRACK_WIDTH_M = 14.68
GAZEBO_TRACK_HEIGHT_M = 14.99
BRAIN_MAP_WIDTH_PX = 5338.0
BRAIN_MAP_HEIGHT_PX = 3541.0
BRAIN_MAP_HEIGHT_M = 15.0
BRAIN_MAP_PIXELS_PER_METER = BRAIN_MAP_HEIGHT_PX / BRAIN_MAP_HEIGHT_M
BRAIN_MAP_WIDTH_M = BRAIN_MAP_WIDTH_PX / BRAIN_MAP_PIXELS_PER_METER
GAZEBO_TO_BRAIN_X_SCALE = BRAIN_MAP_WIDTH_M / GAZEBO_TRACK_WIDTH_M
GAZEBO_TO_BRAIN_Y_SCALE = BRAIN_MAP_HEIGHT_M / GAZEBO_TRACK_HEIGHT_M

# The Gazebo car plugin multiplies its received speed by three before applying
# wheel angular velocity.  AutomobileData and encoder values remain in m/s, so
# compensate only at this transport boundary.
GAZEBO_SPEED_MULTIPLIER = 3.0

# A normal odometry update is only a few millimetres at the simulator update
# rate.  A larger displacement means that the model was reset or teleported;
# it must not be counted as travelled distance.
MAX_ODOMETRY_STEP_M = 1.0


def _simulator_position_to_brain(x: float, y: float) -> tuple[float, float]:
    """Map simulator GPS metres onto the metric frame used by the brain graph."""
    return (
        float(x) * GAZEBO_TO_BRAIN_X_SCALE,
        BRAIN_MAP_HEIGHT_M - float(y) * GAZEBO_TO_BRAIN_Y_SCALE,
    )


def _simulator_world_position_to_brain(
        x: float, world_y: float) -> tuple[float, float]:
    """Map an unmodified Gazebo world position into the Brain graph frame."""
    return (
        float(x) * GAZEBO_TO_BRAIN_X_SCALE,
        BRAIN_MAP_HEIGHT_M + float(world_y) * GAZEBO_TO_BRAIN_Y_SCALE,
    )


def _simulator_yaw_to_brain(yaw: float) -> float:
    """Map Gazebo CCW yaw to the brain graph frame, returning radians.

    Gazebo world y is negative over the track while its GPS plugin publishes
    ``abs(world_y)``.  Position conversion applies ``15 - y_gps * scale``, so
    graph y has the same direction as Gazebo world y. Scaling is anisotropic,
    therefore transform the heading vector before recovering its angle.
    """
    dx = GAZEBO_TO_BRAIN_X_SCALE * math.cos(float(yaw))
    dy = GAZEBO_TO_BRAIN_Y_SCALE * math.sin(float(yaw))
    return math.atan2(dy, dx)


def _normalize_angle(angle: float) -> float:
    """Wrap an angle in radians to [-pi, pi]."""
    return math.atan2(math.sin(float(angle)), math.cos(float(angle)))


def _core_speed_to_simulator(speed: float) -> float:
    """Convert a core m/s request to the plugin's pre-multiplied value."""
    return float(speed) / GAZEBO_SPEED_MULTIPLIER


def _accumulate_odometry_distance(
        total: float,
        previous: tuple[float, float] | None,
        current: tuple[float, float],
) -> tuple[float, tuple[float, float], bool]:
    """Accumulate physical odometry while rejecting reset/teleport jumps.

    The returned boolean is true when the current sample established a new
    origin after a discontinuity and therefore was not added to ``total``.
    """
    current = (float(current[0]), float(current[1]))
    if previous is None:
        return float(total), current, False

    step = math.hypot(
        current[0] - float(previous[0]),
        current[1] - float(previous[1]),
    )
    if not math.isfinite(step) or step > MAX_ODOMETRY_STEP_M:
        return float(total), current, True
    return float(total) + step, current, False


def _yaw_from_quaternion(q) -> float:
    """Return ROS quaternion yaw in radians."""
    siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
    cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
    return math.atan2(siny_cosp, cosy_cosp)


class AutomobileDataSimulator(Automobile_Data, Node):
    """Expose simulator ROS topics through the common AutomobileData API."""

    def __init__(self, trig_control=True, trig_bno=False, trig_enc=False,
                 trig_sonar=False, trig_cam=False, trig_gps=False,
                 trig_lidar=False, trig_tof=False):
        Automobile_Data.__init__(self)
        Node.__init__(self, 'automobile_data_simulator')

        self.frame = None
        self.flag_localisation = False
        self.yaw_true = 0.0
        self.lidar_angles = np.array([])
        self.lidar_ranges = np.array([])
        self._bridge = CvBridge()
        self._speed_buffer = deque(maxlen=20)
        self.x_buffer = deque(maxlen=5)
        self.y_buffer = deque(maxlen=5)
        self.yaw_buffer = deque(maxlen=10)
        self._target_distance = None
        self._has_current_odometry = False
        self._has_global_odometry = False
        self.global_pose_ready = False
        self.global_position_std = float('inf')
        self._use_odometry_for_encoder = bool(trig_enc)
        self._odom_last_position = None

        if trig_control:
            self._command_pub = self.create_publisher(
                String, '/automobile/command', 10)
            self.pub_closest_node = self.create_publisher(
                Float32, '/automobile/closest_node', 1)
            self.pub_path_progress = self.create_publisher(
                Float32, '/automobile/path/progress', 1)
            self.pub_next_event = self.create_publisher(
                String, '/automobile/next_event', 1)
            self.pub_prev_event = self.create_publisher(
                String, '/automobile/prev_event', 1)
            self.pub_current_state = self.create_publisher(
                String, '/automobile/current_state', 1)
            self.pub_routines = self.create_publisher(
                String, '/automobile/routines', 1)
            self.pub_conditions = self.create_publisher(
                Conditions, '/automobile/conditions', 1)
            self.pub_arena = self.create_publisher(Bool, '/automobile/arena', 1)
            self.pub_led = self.create_publisher(Bool, '/automobile/led', 1)
            self.pub_localisation = self.create_publisher(
                Localisation, '/automobile/localisation/estimate', 1)
            self.create_timer(0.02, self._distance_control)

        if trig_cam:
            self.create_subscription(
                Image, '/oak/rgb/image_rect', self._image_callback, 1)
        if trig_bno:
            self.create_subscription(Imu, '/oak/imu/data', self._imu_callback, 10)
        if trig_enc:
            # Encoder state is derived below from the canonical /encoder_odom
            # stream.  Do not subscribe to /automobile/encoder/distance here:
            # each sensor_converter process owns an independent accumulator,
            # so overlapping simulator launches can otherwise interleave two
            # incompatible cumulative distances on the same topic.
            self.reset_rel_pose()
        if trig_enc or trig_gps:
            self.create_subscription(
                Odometry, '/encoder_odom', self._odometry_callback, 10)
        if trig_gps:
            self.create_subscription(
                String, '/automobile/localisation', self._position_callback, 10)
            self.create_subscription(
                Odometry, '/odometry/global', self._global_odometry_callback, 10)
        if trig_lidar:
            self.create_subscription(LaserScan, '/scan', self._lidar_callback, 10)

    def _publish_command(self, action: str, **values):
        payload = {'action': action, **values}
        self._command_pub.publish(String(data=json.dumps(payload)))

    def _image_callback(self, msg: Image):
        self.frame = self._bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    def _imu_callback(self, msg: Imu):
        self.roll = 0.0
        self.pitch = 0.0
        if not self._has_global_odometry:
            simulator_yaw = _yaw_from_quaternion(msg.orientation)
            self.yaw_true = _simulator_yaw_to_brain(simulator_yaw)
            self.yaw = _normalize_angle(self.yaw_true + self.yaw_offset)
            self.yaw_deg = math.degrees(self.yaw)
        self.accel_x = msg.linear_acceleration.x
        self.accel_y = msg.linear_acceleration.y
        self.accel_z = msg.linear_acceleration.z
        self.gyrox = msg.angular_velocity.x
        self.gyroy = msg.angular_velocity.y
        self.gyroz = msg.angular_velocity.z
        if not self._has_global_odometry:
            self.yaw_buffer.append(self.yaw)

    # UNUSED: AutomobileDataSimulator._speed_callback has no production caller.
    # def _speed_callback(self, msg: Float32):
        # self.encoder_velocity = float(msg.data)
        # self._speed_buffer.append(self.encoder_velocity)
        # self.filtered_encoder_velocity = float(np.median(self._speed_buffer))

    # UNUSED: AutomobileDataSimulator._distance_callback has no production caller.
    # def _distance_callback(self, msg: Float32):
        # self.encoder_distance = float(msg.data)
        # self.update_rel_position()

    def _odometry_callback(self, msg: Odometry):
        """Use current simulator odometry for control-state estimation.

        This topic is retained for encoder-distance and speed processing. The
        fused ``/odometry/global`` callback owns ``x_est``/``y_est`` whenever
        localization is active, avoiding direct-GPS control pose updates.
        """
        world_position = (
            float(msg.pose.pose.position.x),
            float(msg.pose.pose.position.y),
        )
        point = _simulator_world_position_to_brain(*world_position)
        if not self._has_global_odometry:
            self.x_est, self.y_est = point
            self.x_true, self.y_true = point
        self._has_current_odometry = True

        if self._use_odometry_for_encoder:
            self.encoder_distance, self._odom_last_position, rejected = (
                _accumulate_odometry_distance(
                    self.encoder_distance,
                    self._odom_last_position,
                    world_position,
                )
            )
            if rejected:
                self.get_logger().warning(
                    'Odometry pose discontinuity ignored while accumulating '
                    'encoder distance')

            self.encoder_velocity = float(msg.twist.twist.linear.x)
            self._speed_buffer.append(self.encoder_velocity)
            self.filtered_encoder_velocity = float(
                np.median(self._speed_buffer))
            self.update_rel_position()

    def _global_odometry_callback(self, msg: Odometry):
        """Use the fused map-frame pose for Brain and random-start."""
        q = msg.pose.pose.orientation
        yaw = _yaw_from_quaternion(q)
        self.x = float(msg.pose.pose.position.x)
        self.y = float(msg.pose.pose.position.y)
        self.x_est = self.x
        self.y_est = self.y
        self.x_true = self.x
        self.y_true = self.y
        self.yaw_true = yaw
        self.yaw = _normalize_angle(yaw + self.yaw_offset)
        self.yaw_est = self.yaw
        self.yaw_deg = math.degrees(self.yaw)
        self.yaw_buffer.append(self.yaw)
        self.global_position_std = math.sqrt(max(
            float(msg.pose.covariance[0]), float(msg.pose.covariance[7])))
        self.global_pose_ready = self.global_position_std <= 0.50
        self._has_global_odometry = True

    def _position_callback(self, msg: String):
        try:
            value = json.loads(msg.data)
            point = _simulator_position_to_brain(value['x'], value['y'])
        except (ValueError, KeyError, TypeError) as exc:
            self.get_logger().warning(f'Invalid localisation payload: {exc}')
            return
        self.x_buffer.append(point[0])
        self.y_buffer.append(point[1])
        self.x = float(np.mean(self.x_buffer))
        self.y = float(np.mean(self.y_buffer))
        if not self._has_current_odometry:
            self.x_est, self.y_est = self.x, self.y
            self.x_true, self.y_true = self.x, self.y
        self.flag_localisation = True

    def _lidar_callback(self, msg: LaserScan):
        self.lidar_angles = np.linspace(msg.angle_min, msg.angle_max, len(msg.ranges))
        self.lidar_ranges = np.asarray(msg.ranges)

    def drive_speed(self, speed=0.0):
        self.speed = Automobile_Data.normalizeSpeed(speed)
        self._target_distance = None
        self._publish_command(
            '1', speed=_core_speed_to_simulator(self.speed))

    def drive_angle(self, angle=0.0):
        self.steer = Automobile_Data.normalizeSteer(angle)
        self._publish_command('2', steerAngle=float(self.steer))

    def stop(self, angle=0.0):
        self.speed = 0.0
        self.steer = Automobile_Data.normalizeSteer(angle)
        self._target_distance = None
        self._publish_command('3', steerAngle=float(self.steer))

    def drive_distance(self, dist=0.0):
        self._target_distance = self.encoder_distance + float(dist)

    def _distance_control(self):
        if self._target_distance is None:
            return
        error = self._target_distance - self.encoder_distance
        if abs(error) < 0.01:
            self.stop(self.steer)
            return
        self.speed = Automobile_Data.normalizeSpeed(
            float(np.clip(0.5 * error, -0.2, 0.2)))
        self._publish_command(
            '1', speed=_core_speed_to_simulator(self.speed))

    def publish_closest_node(self, value=0.0):
        self.pub_closest_node.publish(Float32(data=float(value)))

    def publish_path_progress(self, value=0.0):
        self.pub_path_progress.publish(Float32(data=float(value)))

    def publish_next_event(self, value):
        self.pub_next_event.publish(String(data=str(value)))

    def publish_prev_event(self, value):
        self.pub_prev_event.publish(String(data=str(value)))

    def publish_current_state(self, value):
        self.pub_current_state.publish(String(data=str(value)))

    def publish_routines(self, value):
        self.pub_routines.publish(String(data=str(value)))

    def publish_arena_flag(self, value):
        self.pub_arena.publish(Bool(data=bool(value)))

    def publish_led_control(self, value):
        self.pub_led.publish(Bool(data=bool(value)))

    def publish_conditions(self, value):
        self.pub_conditions.publish(Conditions(**value))

    def publish_localisation(self, x, y):
        self.pub_localisation.publish(Localisation(pos_a=float(x), pos_b=float(y)))
