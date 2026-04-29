#!/usr/bin/env python3
"""
metrics_to_socket.py — ROS2 Jazzy
Collects metrics from all ROS2 topics and sends one JSON blob per tick
to the dashboard via a Unix socket. Faithful port of the ROS1 version.
"""

import argparse
import json
import os
import random
import socket
import time

import numpy as np
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32, String, UInt8, Bool
from utils.msg   import IMU, Conditions

SOCKET_PATH       = "/tmp/metrics_socket.sock"
PUBLISH_RATE_HZ   = 2.0
YAW_GLOBAL_OFFSET = np.deg2rad(0)


# ── Socket sender (unchanged logic from ROS1 version) ────────────────────── #

class MetricSender:
    def __init__(self):
        self.sock      = None
        self.connected = False
        self.connect_to_server()

    def connect_to_server(self):
        while True:
            try:
                if os.path.exists(SOCKET_PATH):
                    self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    self.sock.connect(SOCKET_PATH)
                    self.connected = True
                    print("Connected to receiver.")
                    break
                else:
                    print("Socket file does not exist. Waiting...")
                    time.sleep(3)
            except Exception as e:
                print(f"Connection error: {e}")
                time.sleep(3)

    def send(self, metrics: dict):
        if not self.connected:
            self.connect_to_server()
        try:
            data = json.dumps(metrics).encode('utf-8') + b'\n'
            self.sock.sendall(data)
        except Exception as e:
            print(f"Send failed: {e}")
            self.connected = False

    def close(self):
        if self.sock:
            self.sock.close()
            self.connected = False


# ── Simulated metrics (unchanged from ROS1 version) ──────────────────────── #

def generate_metrics() -> dict:
    return {
        "CHECKPOINT":      random.choice([455, 465, 99]),
        "STATE":           random.choice(["LANE_FOLLOWING", "STOP"]),
        "PREV_EVENT":      None,
        "UPCOMING_EVENT":  random.choice(["STOPLINE", "ROUNDABOUT"]),
        "ROUTINES":        ["FOLLOW_LANE", "DETECT_STOPLINE"],
        "CONDITIONS":      {"CAN_OVERTAKE": True, "HIGHWAY": False},
        "SPEED":           round(random.uniform(0, 5), 2),
        "STEER":           round(random.uniform(-2, 2), 2),
        "YAW":             round(random.uniform(-180, 180), 2),
    }


# ── ROS2 node: caches latest value from every topic ──────────────────────── #

class MetricsToSocket(Node):

    def __init__(self, simulate: bool = False):
        super().__init__('ros_metrics_bridge')
        self._simulate = simulate
        self._sender   = MetricSender()

        # Cache dict — keyed by metric name, value is whatever arrived last
        self._cache: dict = {}

        # ── Subscriptions ─────────────────────────────────────────────── #
        self.create_subscription(String,     '/automobile/current_state',  self._make_cb('STATE',          lambda m: m.data),                   1)
        self.create_subscription(String,     '/automobile/next_event',     self._make_cb('UPCOMING_EVENT', lambda m: m.data),                   1)
        self.create_subscription(String,     '/automobile/prev_event',     self._make_cb('PREV_EVENT',     lambda m: m.data),                   1)
        self.create_subscription(Float32,    '/automobile/closest_node',   self._make_cb('CLOSEST_NODE',   lambda m: m.data),                   1)
        self.create_subscription(Float32,    '/automobile/encoder/speed',  self._make_cb('SPEED',          lambda m: round(m.data, 2)),          1)
        self.create_subscription(Float32,    '/automobile/command/speed',  self._make_cb('SPEED_CMD',      lambda m: round(m.data, 2)),          1)
        self.create_subscription(Float32,    '/automobile/encoder/distance',self._make_cb('DISTANCE',      lambda m: round(m.data, 2)),          1)
        self.create_subscription(Float32,    '/automobile/command/steer',  self._make_cb('STEER',          lambda m: round(m.data, 2)),          1)
        self.create_subscription(UInt8,      '/automobile/tof/front',      self._make_cb('TOF_FRONT',      lambda m: m.data),                   1)
        self.create_subscription(UInt8,      '/automobile/tof/left',       self._make_cb('TOF_LEFT',       lambda m: m.data),                   1)
        self.create_subscription(Bool,       '/automobile/led',            self._make_cb('HEADLIGHTS',     lambda m: m.data),                   1)
        self.create_subscription(Conditions, '/automobile/conditions',     self._conditions_cb,                                                  1)
        self.create_subscription(String,     '/automobile/routines',       self._routines_cb,                                                    1)
        self.create_subscription(IMU,        '/automobile/imu',            self._imu_cb,                                                         1)

        # ── 2 Hz publish timer ────────────────────────────────────────── #
        self.create_timer(1.0 / PUBLISH_RATE_HZ, self._tick)
        self.get_logger().info("metrics_to_socket started")

    # ── Generic callback factory (mirrors safe_wait_for transform logic) ── #

    def _make_cb(self, key: str, transform):
        def cb(msg):
            self._cache[key] = transform(msg)
        return cb

    # ── Special callbacks ─────────────────────────────────────────────── #

    def _conditions_cb(self, msg: Conditions) -> None:
        self._cache['CONDITIONS'] = {
            'CAN_OVERTAKE': msg.can_overtake,
            'HIGHWAY':      msg.highway,
            'CAR_ON_PATH':  msg.car_on_path,
            'REROUTING':    msg.rerouting,
            'TUNNEL':       msg.tunnel,
        }

    def _routines_cb(self, msg: String) -> None:
        # Dashboard expects a list; brain publishes semicolon-separated string
        self._cache['ROUTINES'] = msg.data.split(';')

    def _imu_cb(self, msg: IMU) -> None:
        yaw = float(msg.yaw) + YAW_GLOBAL_OFFSET
        self._cache['YAW'] = round(yaw, 2)
        if   45  <= yaw < 135:
            self._cache['HEADING'] = 'North'
        elif 135 <= yaw < 225:
            self._cache['HEADING'] = 'East'
        elif 225 <= yaw < 315:
            self._cache['HEADING'] = 'South'
        else:
            self._cache['HEADING'] = 'West'

    # ── Timer tick: snapshot cache and send ──────────────────────────── #

    def _tick(self) -> None:
        metrics = generate_metrics() if self._simulate else dict(self._cache)
        if metrics:
            self._sender.send(metrics)

    def destroy_node(self) -> None:
        self._sender.close()
        super().destroy_node()


# ── Entry point ──────────────────────────────────────────────────────────── #

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--simulate', action='store_true')
    parsed, unknown = parser.parse_known_args()

    rclpy.init(args=args)
    node = MetricsToSocket(simulate=parsed.simulate)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()