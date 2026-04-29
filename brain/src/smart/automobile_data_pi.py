#!/usr/bin/env python3
"""
automobile_data_pi.py — ROS2 Jazzy
All publishers, subscribers, and callbacks for the physical car.
"""

import rclpy
from rclpy.node import Node
import collections
import numpy as np

from std_msgs.msg    import Float32, Bool, String, UInt8
from sensor_msgs.msg import LaserScan, Image
from cv_bridge       import CvBridge
from utils.msg       import IMU, Localisation, Vehicles, Conditions

from automobile_data_interface import Automobile_Data
import helper_functions as hf

SONAR_THRESHOLD      = 5
SONAR_DEQUE_LENGTH   = 20
TOF_DEQUE_LENGTH     = 10
IMU_DEQUE_LENGTH     = 10
CLASSIFY_DEQUE_LENGTH = 4


class AutomobileDataPi(Automobile_Data, Node):

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

        Automobile_Data.__init__(self)
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
        self.frame                          = None

        # ── Publishers & subscribers ──────────────────────────────────── #
        if trig_control:
            self.pub_speed         = self.create_publisher(Float32,     '/automobile/command/speed',    1)
            self.pub_steer         = self.create_publisher(Float32,     '/automobile/command/steer',    1)
            self.pub_stop          = self.create_publisher(Float32,     '/automobile/command/stop',     1)
            self.pub_position      = self.create_publisher(Float32,     '/automobile/command/position', 1)
            self.pub_closest_node  = self.create_publisher(Float32,     '/automobile/closest_node',     1)
            self.pub_next_event    = self.create_publisher(String,      '/automobile/next_event',       1)
            self.pub_prev_event    = self.create_publisher(String,      '/automobile/prev_event',       1)
            self.pub_current_state = self.create_publisher(String,      '/automobile/current_state',    1)
            self.pub_routines      = self.create_publisher(String,      '/automobile/routines',         1)
            self.pub_conditions    = self.create_publisher(Conditions,  '/automobile/conditions',       1)
            self.pub_arena         = self.create_publisher(Bool,        '/automobile/arena',            1)
            self.pub_led           = self.create_publisher(Bool,        '/automobile/led',              1)
            # brain publishes its own estimated position here (NOT the GPS input)
            self.pub_localisation  = self.create_publisher(Localisation, '/automobile/localisation',   1)
            self.sub_position      = self.create_subscription(
                Bool, '/automobile/feedback/position', self.feedback_position_callback, 1)

        if trig_bno:
            self.sub_imu = self.create_subscription(
                IMU, '/oak/imu/data', self.imu_callback, 10)

        if trig_enc:
            self.sub_encSpeed = self.create_subscription(
                Float32, '/automobile/encoder/speed',    self.encoder_velocity_callback, 10)
            self.sub_encDist  = self.create_subscription(
                Float32, '/automobile/encoder/distance', self.encoder_distance_callback, 10)
            self.reset_rel_pose()

        if trig_sonar:
            self.sub_son_center = self.create_subscription(
                Float32, '/automobile/sonar/center', self.center_sonar_callback, 1)
            self.sub_son_right  = self.create_subscription(
                Float32, '/automobile/sonar/right',  self.right_sonar_callback,  1)
            self.sub_son_left   = self.create_subscription(
                Float32, '/automobile/sonar/left',   self.left_sonar_callback,   1)

        if trig_cam:
            self._bridge = CvBridge()
            self.create_subscription(
                Image, '/oak/rgb/image_raw', self._image_callback, 1)

        if trig_gps:
            # GPS comes from the competition bridge on this topic (mm → m already converted)
            self.sub_gps = self.create_subscription(
                Localisation, '/automobile/localisation/gps', self.position_callback, 1)

        if trig_lidar:
            self.sub_lidar = self.create_subscription(
                LaserScan, '/scan', self.lidar_callback, 10)

        if trig_tof:
            self.sub_tof_center = self.create_subscription(
                UInt8, '/automobile/tof/front', self.center_tof_callback, 1)
            self.sub_tof_left   = self.create_subscription(
                UInt8, '/automobile/tof/left',  self.left_tof_callback,   1)

    # ═══════════════════════════════════════════════════════════════════ #
    #  SENSOR CALLBACKS                                                   #
    # ═══════════════════════════════════════════════════════════════════ #

    def center_sonar_callback(self, data: Float32) -> None:
        self.center_sonar_distance = data.data if data.data > 0 else self.center_sonar_distance
        self.center_sonar_distance_buffer.append(self.center_sonar_distance)
        self.filtered_center_sonar_distance = np.median(self.center_sonar_distance_buffer)
        self.sonar_distance          = self.center_sonar_distance
        self.filtered_sonar_distance = self.filtered_center_sonar_distance

    def right_sonar_callback(self, data: Float32) -> None:
        self.right_sonar_distance = data.data if data.data > 0 else self.right_sonar_distance
        self.right_sonar_distance_buffer.append(self.right_sonar_distance)
        self.filtered_right_sonar_distance = np.median(self.right_sonar_distance_buffer)

    def left_sonar_callback(self, data: Float32) -> None:
        self.left_sonar_distance = data.data if data.data > 0 else self.left_sonar_distance
        self.left_sonar_distance_buffer.append(self.left_sonar_distance)
        self.filtered_left_sonar_distance = np.median(self.left_sonar_distance_buffer)

    def center_tof_callback(self, data: UInt8) -> None:
        self.center_tof_distance = data.data if data.data > 0 else self.center_tof_distance
        self.center_tof_distance_buffer.append(self.center_tof_distance / 1000.0)  # mm → m
        self.filtered_center_tof_distance = np.median(self.center_tof_distance_buffer)

    def left_tof_callback(self, data: UInt8) -> None:
        self.left_tof_distance = data.data if data.data > 0 else self.left_tof_distance
        self.left_tof_distance_buffer.append(self.left_tof_distance / 1000.0)  # mm → m
        self.filtered_left_tof_distance = np.median(self.left_tof_distance_buffer)

    def lidar_callback(self, data: LaserScan) -> None:
        self.lidar_angles = np.linspace(data.angle_min, data.angle_max, len(data.ranges))
        self.lidar_ranges = np.array(data.ranges)

    def position_callback(self, data: Localisation) -> None:
        """GPS position from competition bridge.
        data.pos_a / pos_b are already in metres (bridge divides mm by 1000).
        """
        pL     = np.array([data.pos_a, data.pos_b])
        pR     = hf.mL2mR(pL)
        tmp_x  = pR[0] - self.WB / 2 * np.cos(self.yaw)
        tmp_y  = pR[1] - self.WB / 2 * np.sin(self.yaw)
        self.x_buffer.append(tmp_x)
        self.y_buffer.append(tmp_y)
        self.x     = np.mean(self.x_buffer)
        self.y     = np.mean(self.y_buffer)
        self.x_est = self.x
        self.y_est = self.y
        self.x_GPS = self.x
        self.y_GPS = self.y
        self.flag_localisation = True

    def imu_callback(self, data: IMU) -> None:
        self.roll      = float(data.roll)
        self.roll_deg  = np.rad2deg(self.roll)
        self.pitch     = float(data.pitch)
        self.pitch_deg = np.rad2deg(self.pitch)
        self.yaw_true  = float(data.yaw)
        self.yaw       = float(data.yaw) + self.yaw_offset
        self.yaw_deg   = np.rad2deg(self.yaw)

    def encoder_distance_callback(self, data: Float32) -> None:
        self.encoder_distance = data.data
        self.update_rel_position()

    def encoder_velocity_callback(self, data: Float32) -> None:
        self.encoder_velocity = data.data
        self.encoder_velocity_buffer.append(self.encoder_velocity)
        self.filtered_encoder_velocity = np.median(self.encoder_velocity_buffer)

    def obstacle_callback(self, data) -> None:
        self.obstacle = data.data
        self.obstacle_buffer.append(self.obstacle)
        self.filtered_obstacle = np.median(self.obstacle_buffer)

    def sign_callback(self, data) -> None:
        self.sign = data.data
        self.sign_buffer.append(self.sign)
        self.filtered_sign = np.median(self.sign_buffer)

    def feedback_position_callback(self, data: Bool) -> None:
        self.reachedPosition = data.data

    def _image_callback(self, msg: Image) -> None:
        self.frame = self._bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

    # ═══════════════════════════════════════════════════════════════════ #
    #  COMMAND ACTIONS                                                    #
    # ═══════════════════════════════════════════════════════════════════ #

    def drive_speed(self, speed: float = 0.0) -> None:
        speed      = Automobile_Data.normalizeSpeed(speed)
        self.speed = speed
        self.pub_speed.publish(Float32(data=float(speed)))

    def drive_angle(self, angle: float = 0.0) -> None:
        angle      = Automobile_Data.normalizeSteer(angle)
        self.steer = angle
        self.pub_steer.publish(Float32(data=float(angle)))

    def stop(self, angle: float = 0.0) -> None:
        angle      = Automobile_Data.normalizeSteer(angle)
        self.steer = angle
        self.pub_stop.publish(Float32(data=float(angle)))

    # ═══════════════════════════════════════════════════════════════════ #
    #  ADDITIONAL METHODS                                                 #
    # ═══════════════════════════════════════════════════════════════════ #

    def drive_distance(self, dist: float = 0.0) -> None:
        self.reachedPosition = False
        self.pub_position.publish(Float32(data=float(dist)))

    def publish_closest_node(self, data: float = 0.0) -> None:
        self.pub_closest_node.publish(Float32(data=float(data)))

    def publish_next_event(self, data: str) -> None:
        self.pub_next_event.publish(String(data=str(data)))

    def publish_prev_event(self, data: str) -> None:
        self.pub_prev_event.publish(String(data=str(data)))

    def publish_current_state(self, data: str) -> None:
        self.pub_current_state.publish(String(data=str(data)))

    def publish_arena_flag(self, data: bool) -> None:
        self.pub_arena.publish(Bool(data=bool(data)))

    def publish_routines(self, data: str) -> None:
        self.pub_routines.publish(String(data=str(data)))

    def publish_conditions(self, data: dict) -> None:
        msg = Conditions(
            can_overtake = bool(data['can_overtake']),
            highway      = bool(data['highway']),
            car_on_path  = bool(data['car_on_path']),
            rerouting    = bool(data['rerouting']),
            tunnel       = bool(data['tunnel']),
        )
        self.pub_conditions.publish(msg)

    def publish_led_control(self, data: bool) -> None:
        self.pub_led.publish(Bool(data=bool(data)))

    def publish_localisation(self, x: float, y: float) -> None:
        """Publish the brain's estimated position (NOT the raw GPS input)."""
        msg = Localisation(
            pos_a     = float(x),
            pos_b     = float(y),
            timestamp = 0.0,
            rot_a     = 0.0,
            rot_b     = 0.0,
        )
        self.pub_localisation.publish(msg)

    def destroy_node(self) -> None:
        super().destroy_node()