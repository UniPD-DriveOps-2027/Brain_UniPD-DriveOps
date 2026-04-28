#!/usr/bin/env python3
"""
imuNODE — ROS2 Jazzy version
Reads IMU data from shared memory and publishes on /automobile/imu
"""

import rclpy
from rclpy.node import Node
from utils.msg import IMU
import mmap

SHM_FILE = "/dev/shm/imu_shared_memory"
YAW_OFFSET = 0.0


def apply_yaw_offset(yaw_value: float, offset: float) -> float:
    adjusted = yaw_value + offset
    while adjusted < 0:
        adjusted += 360.0
    while adjusted >= 360:
        adjusted -= 360.0
    return adjusted


class ImuNode(Node):
    def __init__(self):
        super().__init__('imu_shared_memory_publisher')

        self.pub = self.create_publisher(IMU, '/automobile/imu', 10)

        # Open shared memory once; timer does the polling
        self._shm_file = open(SHM_FILE, "r")
        self._shm = mmap.mmap(self._shm_file.fileno(), 1024, access=mmap.ACCESS_READ)

        # 10 Hz timer
        self.create_timer(0.1, self._timer_cb)
        self.get_logger().info("imuNODE started")

    def _timer_cb(self):
        self._shm.seek(0)
        raw = self._shm.read(1024).decode('utf-8', errors='ignore').split('\x00', 1)[0].strip()
        self.get_logger().debug(f"Raw IMU: '{raw}'")

        values = self._parse(raw)
        if values is None:
            return

        msg = IMU()
        msg.roll   = values[0]
        msg.pitch  = values[1]
        msg.yaw    = apply_yaw_offset(values[2], YAW_OFFSET)
        msg.accelx = values[3]
        msg.accely = values[4]
        msg.accelz = values[5]
        msg.gyrox  = values[6]
        msg.gyroy  = values[7]
        msg.gyroz  = values[8]
        self.pub.publish(msg)

    def _parse(self, data_str: str):
        try:
            parts = [float(x) for x in data_str.strip().split(',')]
            if len(parts) != 9:
                self.get_logger().warn(f"Invalid IMU data length: expected 9, got {len(parts)}")
                return None
            return parts
        except Exception as e:
            self.get_logger().debug(f"IMU parse error: {e}")
            return None

    def destroy_node(self):
        self._shm.close()
        self._shm_file.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = ImuNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
