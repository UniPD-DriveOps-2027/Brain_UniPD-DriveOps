#!/usr/bin/env python3
"""
trafficBridge.py
Starts the unmodified Bosch traffic communication engine
(threadTrafficCommunication / tcpClient / udpListener), drains the location
queue and publishes to the ROS2 topic automobile_data_pi expects.
Also subscribes to the correct ROS2 topics to send telemetry back to the server.

Topics published:
  /automobile/localisation/gps   (utils/Localisation)  ← your car's position from server

Topics subscribed:
  /automobile/encoder/speed      (std_msgs/Float32)     → deviceSpeed  to server
  /automobile/localisation       (utils/Localisation)   → devicePos    to server
  /oak/imu/data                  (utils/IMU)            → deviceRot      to server
  /automobile/environment        (utils/Environmental)  → historyData  to server

CONFIG:
  DEVICE_ID   — your car's localization device ID (shown on the physical device)
  FREQUENCY   — how often you want position updates in seconds (0.1–5.0)
  KEY_PATH    — path to the server public key PEM file
"""

import threading
from multiprocessing import Queue

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

from utils.msg import Localisation, IMU, Environmental

# ── Engine imports (Bosch code, untouched) ────────────────────────────── #
from data.TrafficCommunication.threads.threadTrafficCommunication import threadTrafficCommunication
from data.TrafficCommunication.useful.sharedMem import sharedMem

# ── Config ───────────────────────────────────────────────────────────── #
DEVICE_ID = 1          # Change to your car's ID (shown on the localization device)
FREQUENCY = 1.0        # Position update frequency in seconds (0.1–5.0)
KEY_PATH  = 'src/input/src/data/TrafficCommunication/useful/publickey_server.pem'
# At competition use: 'src/input/src/data/TrafficCommunication/useful/publickey_server.pem'

# msgID from allMessages.py
MSG_ID_LOCATION = 1


class TrafficBridge(Node):

    def __init__(self, queue_list: dict, shared_memory: sharedMem):
        super().__init__('traffic_bridge')
        self._queue_list   = queue_list
        self._shared_memory = shared_memory

        # ── Publisher — GPS position received FROM server ────────────── #
        self._gps_pub = self.create_publisher(
            Localisation, '/automobile/localisation/gps', 1)

        # ── Subscriptions — telemetry TO send to server ──────────────── #
        self.create_subscription(
            Float32, '/automobile/encoder/speed', self._speed_cb, 1)

        self.create_subscription(
            Localisation, '/automobile/localisation', self._pos_cb, 1)

        self.create_subscription(
            IMU, '/oak/imu/data', self._imu_cb, 1)

        self.create_subscription(
            Environmental, '/automobile/environment', self._env_cb, 1)

        # ── Drain thread — location messages coming back from server ─── #
        self._running = True
        self._drain_thread = threading.Thread(target=self._drain, daemon=True)
        self._drain_thread.start()

    # ── Queue drain (location data from server → ROS2) ───────────────── #
    def _drain(self):
        general_q = self._queue_list['General']
        while self._running and rclpy.ok():
            try:
                msg = general_q.get(timeout=1.0)
            except Exception:
                continue

            if msg.get('msgID') != MSG_ID_LOCATION:
                continue

            value = msg.get('msgValue', {})
            if value.get('type') != 'location':
                continue

            ros_msg       = Localisation()
            ros_msg.pos_a = float(value.get('x', 0.0))  # driveops todo check units
            ros_msg.pos_b = float(value.get('y', 0.0))
            self._gps_pub.publish(ros_msg)

    # ── Telemetry callbacks (ROS2 → server) ──────────────────────────── #
    def _speed_cb(self, msg: Float32):
        """Encoder speed (m/s → cm/s as server expects)."""
        self._send('deviceSpeed', [msg.data * 100.0])

    def _pos_cb(self, msg: Localisation):
        """Brain's estimated position in metres."""
        self._send('devicePos', [msg.pos_a, msg.pos_b])

    def _imu_cb(self, msg: IMU):
        """Yaw in degrees, clockwise from start orientation."""
        import math
        yaw_deg = math.degrees(float(msg.yaw)) % 360.0
        self._send('deviceRot', [yaw_deg])

    def _env_cb(self, msg: Environmental):
        """Obstacle encountered — id, x, y."""
        self._send('historyData', [msg.obstacle_id, msg.x, msg.y])

    def _send(self, command: str, values: list):
        self._shared_memory.insert(command, values)

    def destroy_node(self):
        self._running = False
        super().destroy_node()


def main(args=None):
    queue_list   = {
        'Critical': Queue(),
        'Warning':  Queue(),
        'General':  Queue(),
        'Config':   Queue(),
    }
    shared_memory = sharedMem()

    # threadTrafficCommunication inherits ThreadWithStop which never calls thread_work(),
    # so the Twisted reactor must be started explicitly in a daemon thread.
    engine = threadTrafficCommunication(
        shared_memory, queue_list, DEVICE_ID, FREQUENCY, KEY_PATH
    )
    reactor_thread = threading.Thread(
        target=lambda: engine.reactor.run(installSignalHandlers=False),
        daemon=True
    )
    reactor_thread.start()

    rclpy.init(args=args)
    node = TrafficBridge(queue_list, shared_memory)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        engine.stop()
        reactor_thread.join(timeout=2.0)
        rclpy.shutdown()


if __name__ == '__main__':
    main()
