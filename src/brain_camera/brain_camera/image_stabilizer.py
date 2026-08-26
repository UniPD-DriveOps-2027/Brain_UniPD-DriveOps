"""Partially stabilize the RGB image with short-term car-IMU roll and pitch."""

import copy
import math

import cv2
from cv_bridge import CvBridge
from geometry_msgs.msg import Vector3Stamped
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import CameraInfo, Image, Imu

from .geometry import cropped_intrinsics, quaternion_to_roll_pitch, wrap_angle


class ImageStabilizer(Node):
    def __init__(self) -> None:
        super().__init__('oak_image_stabilizer')

        self.declare_parameter('image_topic', '/oak/rgb/image_raw')
        self.declare_parameter('camera_info_topic', '/oak/rgb/camera_info')
        self.declare_parameter('imu_topic', '/automobile/imu/data')
        self.declare_parameter('output_image_topic', '/oak/rgb/image_stabilized')
        self.declare_parameter(
            'output_camera_info_topic', '/oak/rgb/camera_info_stabilized'
        )
        self.declare_parameter('correction_topic', '/oak/rgb/stabilization_correction')
        self.declare_parameter('correction_gain', 0.60)
        self.declare_parameter('attitude_baseline_time_constant_s', 1.0)
        self.declare_parameter('max_correction_deg', 3.0)
        self.declare_parameter('crop_x_fraction', 0.05)
        self.declare_parameter('crop_y_fraction', 0.08)
        self.declare_parameter('imu_timeout_s', 0.20)

        get = self.get_parameter
        self.correction_gain = max(0.0, min(float(get('correction_gain').value), 1.0))
        self.baseline_tau_s = max(
            float(get('attitude_baseline_time_constant_s').value), 1.0e-3
        )
        self.max_correction_rad = math.radians(
            max(float(get('max_correction_deg').value), 0.0)
        )
        self.crop_x_fraction = float(get('crop_x_fraction').value)
        self.crop_y_fraction = float(get('crop_y_fraction').value)
        self.imu_timeout_s = max(float(get('imu_timeout_s').value), 0.0)

        self.bridge = CvBridge()
        self.camera_info = None
        self.roll_baseline = None
        self.pitch_baseline = None
        self.roll_vibration = 0.0
        self.pitch_vibration = 0.0
        self.last_imu_stamp_ns = None
        self.last_imu_receive_ns = None

        self.image_publisher = self.create_publisher(
            Image, get('output_image_topic').value, 1
        )
        self.info_publisher = self.create_publisher(
            CameraInfo, get('output_camera_info_topic').value, 1
        )
        self.correction_publisher = self.create_publisher(
            Vector3Stamped, get('correction_topic').value, 10
        )
        self.image_subscription = self.create_subscription(
            Image,
            get('image_topic').value,
            self.image_callback,
            qos_profile_sensor_data,
        )
        self.info_subscription = self.create_subscription(
            CameraInfo,
            get('camera_info_topic').value,
            self.camera_info_callback,
            qos_profile_sensor_data,
        )
        self.imu_subscription = self.create_subscription(
            Imu, get('imu_topic').value, self.imu_callback, qos_profile_sensor_data
        )

        self.get_logger().info(
            'Camera stabilizer: %s -> %s (gain %.0f%%, crop %.0f%%/%.0f%%)'
            % (
                get('image_topic').value,
                get('output_image_topic').value,
                self.correction_gain * 100.0,
                self.crop_x_fraction * 100.0,
                self.crop_y_fraction * 100.0,
            )
        )

    def camera_info_callback(self, message: CameraInfo) -> None:
        self.camera_info = copy.deepcopy(message)

    def imu_callback(self, message: Imu) -> None:
        if message.orientation_covariance[0] < 0.0:
            return
        try:
            roll, pitch = quaternion_to_roll_pitch(
                message.orientation.x,
                message.orientation.y,
                message.orientation.z,
                message.orientation.w,
            )
        except ValueError:
            return

        stamp_ns = int(message.header.stamp.sec) * 1_000_000_000 + int(
            message.header.stamp.nanosec
        )
        if stamp_ns <= 0:
            stamp_ns = self.get_clock().now().nanoseconds
        if self.last_imu_stamp_ns is None:
            dt_s = 0.01
        else:
            dt_s = (stamp_ns - self.last_imu_stamp_ns) * 1.0e-9
            if not math.isfinite(dt_s) or dt_s <= 0.0:
                dt_s = 0.01
        self.last_imu_stamp_ns = stamp_ns
        self.last_imu_receive_ns = self.get_clock().now().nanoseconds

        if self.roll_baseline is None:
            self.roll_baseline = roll
            self.pitch_baseline = pitch
            return

        alpha = 1.0 - math.exp(-min(dt_s, 1.0) / self.baseline_tau_s)
        roll_delta = wrap_angle(roll - self.roll_baseline)
        pitch_delta = wrap_angle(pitch - self.pitch_baseline)
        self.roll_baseline = wrap_angle(self.roll_baseline + alpha * roll_delta)
        self.pitch_baseline = wrap_angle(self.pitch_baseline + alpha * pitch_delta)
        self.roll_vibration = wrap_angle(roll - self.roll_baseline)
        self.pitch_vibration = wrap_angle(pitch - self.pitch_baseline)

    def active_corrections(self):
        if self.last_imu_receive_ns is None:
            return 0.0, 0.0
        age_s = (
            self.get_clock().now().nanoseconds - self.last_imu_receive_ns
        ) * 1.0e-9
        if age_s > self.imu_timeout_s:
            return 0.0, 0.0
        limit = self.max_correction_rad
        roll = max(-limit, min(limit, self.correction_gain * self.roll_vibration))
        pitch = max(-limit, min(limit, self.correction_gain * self.pitch_vibration))
        return roll, pitch

    def image_callback(self, message: Image) -> None:
        if self.camera_info is None:
            return
        try:
            frame = self.bridge.imgmsg_to_cv2(message, desired_encoding='bgr8')
        except Exception as error:
            self.get_logger().warning('Image conversion failed: %s' % error)
            return

        height, width = frame.shape[:2]
        info = copy.deepcopy(self.camera_info)
        k_out, p_out, crop_x, crop_y = cropped_intrinsics(
            info.k,
            info.p,
            width,
            height,
            self.crop_x_fraction,
            self.crop_y_fraction,
        )
        roll_correction, pitch_correction = self.active_corrections()

        centre = (float(info.k[2]), float(info.k[5]))
        transform = cv2.getRotationMatrix2D(
            centre, math.degrees(roll_correction), 1.0
        )
        transform[1, 2] += float(info.k[4]) * math.tan(pitch_correction)
        stabilized = cv2.warpAffine(
            frame,
            transform,
            (width, height),
            flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_REPLICATE,
        )

        inner = stabilized[crop_y:height - crop_y, crop_x:width - crop_x]
        if inner.size == 0:
            return
        stabilized = cv2.resize(inner, (width, height), interpolation=cv2.INTER_LINEAR)

        output = self.bridge.cv2_to_imgmsg(stabilized, encoding='bgr8')
        output.header = message.header
        output.header.frame_id = 'oak_rgb_stabilized'
        self.image_publisher.publish(output)

        info.header = output.header
        info.width = width
        info.height = height
        info.k = k_out
        info.p = p_out
        self.info_publisher.publish(info)

        correction = Vector3Stamped()
        correction.header = output.header
        correction.vector.x = roll_correction
        correction.vector.y = pitch_correction
        correction.vector.z = self.correction_gain
        self.correction_publisher.publish(correction)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = ImageStabilizer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
