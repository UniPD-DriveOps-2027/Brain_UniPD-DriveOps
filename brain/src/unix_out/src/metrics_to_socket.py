#!/usr/bin/env python3
import rospy
import socket
import json
import time
import os
import random
import argparse
import numpy as np
from utils.msg import IMU, localisation, vehicles
from std_msgs.msg import Float32, String

SOCKET_PATH = "/tmp/metrics_socket.sock"

YAW_GLOBAL_OFFSET = np.deg2rad(0)

class MetricSender:
    def __init__(self):
        self.sock = None
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

    def send(self, metrics):
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

def generate_metrics():
    return {
        "CHECKPOINT": random.choice([455, 465, 99]),
        "STATE": random.choice(["LANE_FOLLOWING", "STOP"]),
        "PREV_EVENT": None,
        "UPCOMING_EVENT": random.choice(["STOPLINE", "ROUNDABOUT"]),
        "ROUTINES": ["FOLLOW_LANE", "DETECT_STOPLINE"],
        "CONDITIONS": {"CAN_OVERTAKE": True, "HIGHWAY": False},
        "SPEED": round(random.uniform(0, 5), 2),
        "STEER": round(random.uniform(-2, 2), 2),
        "YAW": round(random.uniform(-180, 180), 2),
    }

def safe_wait_for(topic, msg_type, timeout=0.1, field=None, transform=lambda x: x, name=None):
    try:
        msg = rospy.wait_for_message(topic, msg_type, timeout=timeout)
        value = getattr(msg, field) if field else msg
        return transform(value)
    except rospy.ROSException:
        #rospy.logwarn(f"Timeout on {name or topic}")
        return None

def get_real_metrics():
    metrics = {}
    # METRICS FROM BRAIN
    if (state := safe_wait_for("/automobile/current_state", String, field="data", name="state")) is not None:
        metrics["STATE"] = state
    if (next_event := safe_wait_for("/automobile/next_event", String, field="data", name="next_event")) is not None:
        metrics["UPCOMING_EVENT"] = next_event
    if (prev_event := safe_wait_for("/automobile/prev_event", String, field="data", name="prev_event")) is not None:
        metrics["PREV_EVENT"] = prev_event
    if (closest_node := safe_wait_for("/automobile/closest_node", Float32, field="data", name="closest_node")) is not None:
        metrics["CLOSEST_NODE"] = state

    # TELEMETRY
    if (speed := safe_wait_for("/automobile/encoder/speed", Float32, field="data", name="speed")) is not None:
        metrics["SPEED"] = round(speed, 2)
    if (speed := safe_wait_for("/automobile/encoder/distance", Float32, field="data", name="distance")) is not None:
        metrics["DISTANCE"] = round(speed, 2)
    if (steer := safe_wait_for("/automobile/command/steer", Float32, field="data", name="steer")) is not None:
        metrics["STEER"] = round(steer, 2)

    yaw = safe_wait_for("/automobile/imu", IMU, field="yaw", transform=lambda y: y + YAW_GLOBAL_OFFSET, name="imu")
    if yaw is not None:
        metrics["YAW"] = round(yaw, 2)
        if 45 <= yaw < 135:
            metrics["HEADING"] = "North"
        elif 135 <= yaw < 225:
            metrics["HEADING"] = "East"
        elif 225 <= yaw < 315:
            metrics["HEADING"] = "South"
        else:
            metrics["HEADING"] = "West"

    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--simulate", action="store_true")
    args = parser.parse_args()

    rospy.init_node("ros_metrics_bridge", anonymous=True)
    sender = MetricSender()

    try:
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
            metrics = generate_metrics() if args.simulate else get_real_metrics()
            if metrics:
                sender.send(metrics)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
    finally:
        sender.close()
