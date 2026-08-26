"""Publish vehicle-vibration RMS values from the hardware-compatible IMU."""

import math

import rclpy
from geometry_msgs.msg import Vector3Stamped
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Imu

from .filter import ExponentialVibrationEstimator


class VibrationMonitor(Node):
    def __init__(self) -> None:
        super().__init__('vibration_monitor')

        self.declare_parameter('imu_topic', '/automobile/imu/data')
        self.declare_parameter(
            'linear_rms_topic',
            '/automobile/vibration/linear_acceleration_rms',
        )
        self.declare_parameter(
            'angular_rms_topic',
            '/automobile/vibration/angular_velocity_rms',
        )
        self.declare_parameter('filter_time_constant_s', 0.5)
        self.declare_parameter('publish_rate_hz', 20.0)
        self.declare_parameter('minimum_samples', 10)

        get = self.get_parameter
        time_constant_s = float(get('filter_time_constant_s').value)
        self.minimum_samples = max(2, int(get('minimum_samples').value))
        self.linear_filter = ExponentialVibrationEstimator(time_constant_s)
        self.angular_filter = ExponentialVibrationEstimator(time_constant_s)

        self.linear_publisher = self.create_publisher(
            Vector3Stamped, get('linear_rms_topic').value, 10
        )
        self.angular_publisher = self.create_publisher(
            Vector3Stamped, get('angular_rms_topic').value, 10
        )
        self.subscription = self.create_subscription(
            Imu,
            get('imu_topic').value,
            self.imu_callback,
            qos_profile_sensor_data,
        )

        publish_rate_hz = max(float(get('publish_rate_hz').value), 1.0)
        self.timer = self.create_timer(1.0 / publish_rate_hz, self.publish_metrics)
        self.last_stamp_ns = None
        self.latest_header = None
        self.linear_available = False
        self.angular_available = False

        self.get_logger().info(
            'Vibration monitor: %s -> %s and %s'
            % (
                get('imu_topic').value,
                get('linear_rms_topic').value,
                get('angular_rms_topic').value,
            )
        )

    def imu_callback(self, msg: Imu) -> None:
        stamp_ns = int(msg.header.stamp.sec) * 1_000_000_000 + int(
            msg.header.stamp.nanosec
        )
        if stamp_ns <= 0:
            stamp_ns = self.get_clock().now().nanoseconds
        if self.last_stamp_ns is None:
            dt_s = 0.01
        else:
            dt_s = (stamp_ns - self.last_stamp_ns) * 1.0e-9
            if not math.isfinite(dt_s) or dt_s <= 0.0:
                dt_s = 0.01
        self.last_stamp_ns = stamp_ns
        self.latest_header = msg.header

        # In sensor_msgs/Imu a first covariance value of -1 marks the whole
        # vector unavailable. Do not manufacture vibration data in that case.
        if msg.linear_acceleration_covariance[0] >= 0.0:
            self.linear_filter.update(
                (
                    msg.linear_acceleration.x,
                    msg.linear_acceleration.y,
                    msg.linear_acceleration.z,
                ),
                dt_s,
            )
            self.linear_available = True

        if msg.angular_velocity_covariance[0] >= 0.0:
            self.angular_filter.update(
                (
                    msg.angular_velocity.x,
                    msg.angular_velocity.y,
                    msg.angular_velocity.z,
                ),
                dt_s,
            )
            self.angular_available = True

    @staticmethod
    def make_message(header, values) -> Vector3Stamped:
        message = Vector3Stamped()
        message.header = header
        message.vector.x = values[0]
        message.vector.y = values[1]
        message.vector.z = values[2]
        return message

    def publish_metrics(self) -> None:
        if self.latest_header is None:
            return
        if (
            self.linear_available
            and self.linear_filter.sample_count >= self.minimum_samples
        ):
            self.linear_publisher.publish(
                self.make_message(self.latest_header, self.linear_filter.rms)
            )
        if (
            self.angular_available
            and self.angular_filter.sample_count >= self.minimum_samples
        ):
            self.angular_publisher.publish(
                self.make_message(self.latest_header, self.angular_filter.rms)
            )


def main(args=None) -> None:
    rclpy.init(args=args)
    node = VibrationMonitor()
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
