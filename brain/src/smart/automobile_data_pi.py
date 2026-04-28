#!/usr/bin/env python3
"""
automobile_data_pi — ROS2 Jazzy version
Partial file: __init__ method with all ROS2 publisher/subscriber wiring.
Replace the __init__ body in automobile_data_pi.py with this content.
The rest of the class (callbacks, methods) is unchanged.
"""

# ── Imports ───────────────────────────────────────────────────────────────── #
import rclpy
from rclpy.node import Node
import collections
import numpy as np

from std_msgs.msg    import Float32, Bool, String, UInt8
from sensor_msgs.msg import LaserScan
from utils.msg       import IMU, Localisation, Vehicles, Conditions

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from automobile_data_interface import Automobile_Data

SONAR_THRESHOLD      = 5
SONAR_DEQUE_LENGTH   = 20
TOF_DEQUE_LENGTH     = 10
IMU_DEQUE_LENGTH     = 10
CLASSIFY_DEQUE_LENGTH = 4


class AutomobileDataPi(Automobile_Data, Node):
    """
    ROS2 version: inherit from both Automobile_Data (interface) and Node.

    Usage in main_brain.py:
        rclpy.init()
        car = AutomobileDataPi(trig_control=True, trig_bno=True, ...)
        executor = rclpy.executors.SingleThreadedExecutor()
        executor.add_node(car)
        # spin executor in a background thread while your main loop runs
        spin_thread = threading.Thread(target=executor.spin, daemon=True)
        spin_thread.start()
    """

    def __init__(self,
                 trig_control: bool = True,
                 trig_bno:     bool = False,
                 trig_enc:     bool = False,
                 trig_sonar:   bool = False,
                 trig_cam:     bool = False,
                 trig_gps:     bool = False,
                 trig_lidar:   bool = False,
                 trig_tof:     bool = False,
                 ) -> None:

        # Initialise the pure-Python interface first (sets up non-ROS state)
        Automobile_Data.__init__(self)
        # Then initialise the ROS2 Node
        Node.__init__(self, 'AutomobileDataPi')

        self.YAW_GLOBAL_OFFSET = -90  # degrees — change before starting

        # ── Extra buffers ─────────────────────────────────────────────── #
        self.right_sonar_distance_buffer    = collections.deque(maxlen=SONAR_DEQUE_LENGTH)
        self.left_sonar_distance_buffer     = collections.deque(maxlen=SONAR_DEQUE_LENGTH)
        self.center_sonar_distance          = 3.0
        self.center_sonar_distance_buffer   = collections.deque(maxlen=SONAR_DEQUE_LENGTH)
        self.filtered_center_sonar_distance = 3.0
        self.center_tof_distance_buffer     = collections.deque(maxlen=TOF_DEQUE_LENGTH)
        self.left_tof_distance_buffer       = collections.deque(maxlen=TOF_DEQUE_LENGTH)
        self.encoder_velocity_buffer        = collections.deque(maxlen=SONAR_DEQUE_LENGTH)
        self.reachedPosition                = False
        self.obstacle_buffer                = collections.deque(maxlen=CLASSIFY_DEQUE_LENGTH)
        self.sign_buffer                    = collections.deque(maxlen=CLASSIFY_DEQUE_LENGTH)
        self.is_position_reliable           = True
        self.estimation_last_encoder_distance = 0.0
        self.estimation_last_yaw_est        = 0.0
        self.x_buffer                       = collections.deque(maxlen=5)
        self.y_buffer                       = collections.deque(maxlen=5)
        self.yaw_buffer                     = collections.deque(maxlen=IMU_DEQUE_LENGTH)
        self.lidar_angles                   = 0
        self.lidar_ranges                   = 0
        self.yaw_true                       = 0.0
        self.flag_localisation              = False

        # ── ROS2 publishers & subscribers ────────────────────────────── #
        if trig_control:
            self.pub_speed         = self.create_publisher(Float32,    '/automobile/command/speed',    1)
            self.pub_steer         = self.create_publisher(Float32,    '/automobile/command/steer',    1)
            self.pub_stop          = self.create_publisher(Float32,    '/automobile/command/stop',     1)
            self.pub_position      = self.create_publisher(Float32,    '/automobile/command/position', 1)
            self.pub_closest_node  = self.create_publisher(Float32,    '/automobile/closest_node',     1)
            self.pub_next_event    = self.create_publisher(String,     '/automobile/next_event',       1)
            self.pub_prev_event    = self.create_publisher(String,     '/automobile/prev_event',       1)
            self.pub_current_state = self.create_publisher(String,     '/automobile/current_state',    1)
            self.pub_routines      = self.create_publisher(String,     '/automobile/routines',         1)
            self.pub_conditions    = self.create_publisher(Conditions, '/automobile/conditions',       1)
            self.pub_arena         = self.create_publisher(Bool,       '/automobile/arena',            1)
            self.pub_led           = self.create_publisher(Bool,       '/automobile/led',              1)
            self.pub_localisation  = self.create_publisher(Localisation, '/automobile/localisation',  1)
            self.sub_position      = self.create_subscription(
                Bool, '/automobile/feedback/position', self.feedback_position_callback, 1)

        if trig_bno:
            self.sub_imu = self.create_subscription(
                IMU, '/automobile/imu', self.imu_callback, 10)

        if trig_enc:
            self.sub_encSpeed = self.create_subscription(
                Float32, '/automobile/encoder/speed', self.encoder_velocity_callback, 10)
            self.sub_encDist = self.create_subscription(
                Float32, '/automobile/encoder/distance', self.encoder_distance_callback, 10)
            self.reset_rel_pose()

        if trig_sonar:
            self.sub_son_center = self.create_subscription(
                Float32, '/automobile/sonar/center', self.center_sonar_callback, 1)
            self.sub_son_right  = self.create_subscription(
                Float32, '/automobile/sonar/right',  self.right_sonar_callback, 1)
            self.sub_son_left   = self.create_subscription(
                Float32, '/automobile/sonar/left',   self.left_sonar_callback, 1)

        if trig_cam:
            self._bridge = CvBridge()
            self.frame = None
            self.create_subscription(Image, '/automobile/camera/image_raw', self._image_callback, 1)

        if trig_gps:
            self.sub_gps = self.create_subscription(
                Localisation, '/automobile/localisation', self.gps_callback, 1)

        if trig_lidar:
            self.sub_lidar = self.create_subscription(
                LaserScan, '/scan', self.lidar_callback, 10)

        if trig_tof:
            self.sub_tof_center = self.create_subscription(
                Float32, '/automobile/tof/center', self.center_tof_callback, 1)
            self.sub_tof_left   = self.create_subscription(
                Float32, '/automobile/tof/left',   self.left_tof_callback, 1)

    # ── Helper: publish wrappers (same API as before) ─────────────────── #
    def publish_speed(self, val: float):
        self.pub_speed.publish(Float32(data=float(val)))

    def publish_steer(self, val: float):
        self.pub_steer.publish(Float32(data=float(val)))

    def publish_stop(self, val: float = 0.0):
        self.pub_stop.publish(Float32(data=float(val)))
    def _image_callback(self, msg: Image):
        self.frame = self._bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    # ── Note on message field names ───────────────────────────────────── #
    # ROS2 auto-generates Python fields from the .msg file exactly as written.
    # If your .msg uses posA/posB, the Python field is also posA/posB.
    # Verify after building with: ros2 interface show utils/msg/Localisation
