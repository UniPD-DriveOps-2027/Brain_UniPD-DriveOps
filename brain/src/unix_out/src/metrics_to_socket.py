#!/usr/bin/env python3
import rospy
import socket
import json
import time
import os
import random
import argparse
import numpy as np
from utils.msg import IMU, localisation, vehicles, conditions
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
    
# wrap our own round function
def round2(x): return round(x, 2)

def get_real_metrics():
    metrics = {}

    metric_definitions = [
        # BRAIN STATES
        ("STATE", "/automobile/current_state", String, "data"),
        ("UPCOMING_EVENT", "/automobile/next_event", String, "data"),
        ("PREV_EVENT", "/automobile/prev_event", String, "data"),
        ("CLOSEST_NODE", "/automobile/closest_node", Float32, "data"),
        
        # CONDITIONS
        ("CONDITIONS", "/automobile/conditions", conditions, None),

        # TELEMETRY
        ("SPEED", "/automobile/encoder/speed", Float32, "data", round2),
        ("DISTANCE", "/automobile/encoder/distance", Float32, "data", round2),
        ("STEER", "/automobile/command/steer", Float32, "data", round2),
    ]

    for name, topic, msg_type, field, *transform in metric_definitions:
        value = safe_wait_for(topic, msg_type, field=field, name=name,
                              transform=transform[0] if transform else lambda x: x)
        if value is not None:
            metrics[name] = value

    # Special handling for conditions to convert to dictionary
    if "CONDITIONS" in metrics:
        conditions_msg = metrics["CONDITIONS"]
        metrics["CONDITIONS"] = {
            "CAN_OVERTAKE": conditions_msg.can_overtake,
            "HIGHWAY": conditions_msg.highway,
            "CAR_ON_PATH": conditions_msg.car_on_path,
            "REROUTING": conditions_msg.rerouting,
            "TUNNEL": conditions_msg.tunnel
        }

    # YAW and HEADING separately due to custom logic
    yaw = safe_wait_for("/automobile/imu", IMU, field="yaw",
                        transform=lambda y: y + YAW_GLOBAL_OFFSET, name="imu")
    if yaw is not None:
        #print(f"Yaw: {yaw}")
        metrics["YAW"] = round(yaw, 2)
        if 45 <= yaw < 135:
            metrics["HEADING"] = "North"
        elif 135 <= yaw < 225:
            metrics["HEADING"] = "East"
        elif 225 <= yaw < 315:
            metrics["HEADING"] = "South"
        else:
            metrics["HEADING"] = "West"

    # Custom logic again... read the ROUTINES as a semicolon-separated string
    if (routines_str := safe_wait_for("/automobile/routines", String, field="data", name="routines")) is not None:
        metrics["ROUTINES"] = routines_str.split(";")  # Convert it back to a list

    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--simulate", action="store_true")
    args, unknown = parser.parse_known_args()


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
