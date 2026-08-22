#!/usr/bin/env python3
# Purpose: Forward ROS lidar scans to a Unix-domain dashboard socket.
# Inputs: LaserScan/point data and socket configuration.
# Outputs: Serialised lidar data written to a Unix socket.

"""
lidar_to_socket — ROS2 Jazzy version
Subscribes to /scan, forwards close-range points to a Unix socket.
"""

import socket
import json
import math
import time

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

SOCKET_PATH       = "/tmp/lidar_socket.sock"
MAX_DISTANCE      = 0.65   # metres
ANGLE_MIN_DEG     = 45     # front-right
ANGLE_MAX_DEG     = 315    # front-left


class LidarToSocket(Node):
    def __init__(self):
        super().__init__('lidar_to_socket_node')

        self._sock      = None
        self._connected = False
        self._connect()

        self.create_subscription(LaserScan, '/scan', self._scan_cb, 10)
        self.get_logger().info("lidar_to_socket_node started")

    # ------------------------------------------------------------------ #
    def _connect(self):
        while rclpy.ok():
            try:
                self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self._sock.connect(SOCKET_PATH)
                self._connected = True
                self.get_logger().info(f"Connected to Unix socket: {SOCKET_PATH}")
                return
            except socket.error as e:
                self.get_logger().warn(f"Socket not ready, retrying in 2 s... ({e})")
                time.sleep(2)

    def _scan_cb(self, scan: LaserScan):
        if not self._connected:
            return

        data   = []
        angle  = scan.angle_min
        for r in scan.ranges:
            if scan.range_min < r < min(scan.range_max, MAX_DISTANCE):
                deg = math.degrees(angle) % 360
                if ANGLE_MIN_DEG <= deg <= ANGLE_MAX_DEG:
                    data.append({'angle': round(deg, 2), 'distance': round(r, 3)})
            angle += scan.angle_increment

        if not data:
            return

        try:
            self._sock.sendall((json.dumps(data) + '\n').encode())
        except socket.error as e:
            self.get_logger().warn(f"Lost socket connection: {e}")
            self._connected = False
            self._sock.close()
            self._connect()

    def destroy_node(self):
        if self._sock:
            self._sock.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = LidarToSocket()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
