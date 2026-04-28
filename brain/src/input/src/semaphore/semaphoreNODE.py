#!/usr/bin/env python3
"""
semaphoreNODE — ROS2 Jazzy version
Listens on UDP and publishes semaphore states.
"""

import socket
import json
import threading

import rclpy
from rclpy.node import Node
from std_msgs.msg import Byte


class SemaphoreNode(Node):
    def __init__(self):
        super().__init__('semaphoreNODE')

        self.master_pub      = self.create_publisher(Byte, '/automobile/semaphore/master',     1)
        self.slave_pub       = self.create_publisher(Byte, '/automobile/semaphore/slave',      1)
        self.antimaster_pub  = self.create_publisher(Byte, '/automobile/semaphore/antimaster', 1)
        self.start_pub       = self.create_publisher(Byte, '/automobile/semaphore/start',      1)

        self._init_socket()

        # Run blocking UDP recv in a daemon thread
        self._thread = threading.Thread(target=self._getting, daemon=True)
        self._thread.start()
        self.get_logger().info("semaphoreNODE started")

    def _init_socket(self):
        self._PORT = 50007
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self._sock.bind(('', self._PORT))
        self._sock.settimeout(1)

    def _getting(self):
        while rclpy.ok():
            try:
                data, _ = self._sock.recvfrom(4096)
                dat = json.loads(data.decode('utf-8'))
                id_    = int(dat['id'])
                state  = int(dat['state'])
                msg = Byte(data=state)
                if id_ == 4:
                    self.master_pub.publish(msg)
                elif id_ == 2:
                    self.slave_pub.publish(msg)
                elif id_ == 1:
                    self.antimaster_pub.publish(msg)
                elif id_ == 3:
                    self.start_pub.publish(msg)
            except socket.timeout:
                pass
            except Exception as e:
                self.get_logger().error(f"Receiving data failed: {e}")

    def destroy_node(self):
        self._sock.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SemaphoreNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
