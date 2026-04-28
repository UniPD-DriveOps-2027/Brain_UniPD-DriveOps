#!/usr/bin/env python3
import socket, json, threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan  # if you forward lidar metrics too
from utils.msg import IMU

SOCKET_PATH = "/tmp/metrics_socket.sock"

class MetricsToSocket(Node):
    def __init__(self):
        super().__init__('metrics_to_socket_node')
        self._sock = None
        self._connect()

        self.create_subscription(Float32, '/automobile/encoder/speed',    self._cb_factory('speed'), 1)
        self.create_subscription(Float32, '/automobile/encoder/distance', self._cb_factory('distance'), 1)
        self.create_subscription(IMU,     '/automobile/imu',              self._imu_cb, 1)
        self.get_logger().info("metrics_to_socket started")

    def _connect(self):
        import time
        while rclpy.ok():
            try:
                self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self._sock.connect(SOCKET_PATH)
                return
            except socket.error:
                self.get_logger().warn("Socket not ready, retrying...")
                time.sleep(2)

    def _send(self, data: dict):
        if not self._sock:
            return
        try:
            self._sock.sendall((json.dumps(data) + '\n').encode())
        except socket.error as e:
            self.get_logger().warn(f"Socket error: {e}")
            self._connect()

    def _cb_factory(self, key):
        def cb(msg):
            self._send({key: msg.data})
        return cb

    def _imu_cb(self, msg: IMU):
        self._send({'roll': msg.roll, 'pitch': msg.pitch, 'yaw': msg.yaw})

def main(args=None):
    rclpy.init(args=args)
    node = MetricsToSocket()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()