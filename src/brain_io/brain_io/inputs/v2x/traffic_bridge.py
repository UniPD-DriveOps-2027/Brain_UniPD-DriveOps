# Purpose: Bridge Bosch traffic/V2X communication into ROS 2.
# Inputs: TCP/UDP V2X packets, public key, device ID, and localisation/IMU state.
# Outputs: Vehicle, environmental, and traffic-related ROS messages.


"""ROS 2 bridge for the BFMC traffic/localisation service."""

import math
import threading
from multiprocessing import Queue
from pathlib import Path

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32

from brain_interfaces.msg import Environmental, Localisation
from brain_io.inputs.v2x.TrafficCommunication.threads.threadTrafficCommunication import (
    threadTrafficCommunication,
)
from brain_io.inputs.v2x.TrafficCommunication.useful.sharedMem import sharedMem


MSG_ID_LOCATION = 1
DEFAULT_KEY = str(
    Path(__file__).parent / 'TrafficCommunication/useful/publickey_server.pem')


class TrafficBridge(Node):
    def __init__(self):
        super().__init__('traffic_bridge')
        self.declare_parameter('device_id', 3)
        self.declare_parameter('frequency', 1.0)
        self.declare_parameter('key_path', DEFAULT_KEY)
        self.declare_parameter('localisation_scale', 0.001)

        self._scale = float(self.get_parameter('localisation_scale').value)
        self._queues = {
            name: Queue() for name in ('Critical', 'Warning', 'General', 'Config')
        }
        self._shared_memory = sharedMem()
        self._engine = threadTrafficCommunication(
            self._shared_memory,
            self._queues,
            int(self.get_parameter('device_id').value),
            float(self.get_parameter('frequency').value),
            str(self.get_parameter('key_path').value),
        )
        self._reactor_thread = threading.Thread(
            target=lambda: self._engine.reactor.run(installSignalHandlers=False),
            daemon=True,
        )
        self._reactor_thread.start()

        self._gps_pub = self.create_publisher(
            Localisation, '/automobile/localisation/gps', 1)
        self.create_subscription(
            Float32, '/automobile/encoder/speed', self._speed_cb, 1)
        self.create_subscription(
            Localisation, '/automobile/localisation/estimate', self._pos_cb, 1)
        self.create_subscription(Imu, '/oak/imu/data', self._imu_cb, 1)
        self.create_subscription(
            Environmental, '/automobile/environment', self._env_cb, 1)

        self._running = True
        self._drain_thread = threading.Thread(target=self._drain, daemon=True)
        self._drain_thread.start()

    def _drain(self):
        queue = self._queues['General']
        while self._running and rclpy.ok():
            try:
                msg = queue.get(timeout=1.0)
            except Exception:
                continue
            if msg.get('msgID') != MSG_ID_LOCATION:
                continue
            value = msg.get('msgValue', {})
            if value.get('type') != 'location':
                continue
            self._gps_pub.publish(Localisation(
                pos_a=float(value.get('x', 0.0)) * self._scale,
                pos_b=float(value.get('y', 0.0)) * self._scale,
            ))

    def _speed_cb(self, msg: Float32):
        self._send('deviceSpeed', [msg.data * 100.0])

    def _pos_cb(self, msg: Localisation):
        self._send('devicePos', [msg.pos_a, msg.pos_b])

    def _imu_cb(self, msg: Imu):
        q = msg.orientation
        yaw = math.atan2(
            2.0 * (q.w * q.z + q.x * q.y),
            1.0 - 2.0 * (q.y * q.y + q.z * q.z),
        )
        self._send('deviceRot', [math.degrees(yaw) % 360.0])

    def _env_cb(self, msg: Environmental):
        self._send('historyData', [msg.obstacle_id, msg.x, msg.y])

    def _send(self, command, values):
        self._shared_memory.insert(command, values)

    def destroy_node(self):
        self._running = False
        self._engine.stop()
        self._reactor_thread.join(timeout=2.0)
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = TrafficBridge()
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