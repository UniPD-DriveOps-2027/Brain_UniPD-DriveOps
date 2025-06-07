#!/usr/bin/env python3
import rospy
import socket
import json
import math
import time
from sensor_msgs.msg import LaserScan

SOCKET_PATH = "/tmp/lidar_socket.sock"
MAX_DISTANCE_TO_SEND = 0.65  # meters
ANGLE_MIN_DEG = 45           # front right
ANGLE_MAX_DEG = 315          # front left

class LidarToSocket:
    def __init__(self):
        rospy.init_node('lidar_to_socket_node', anonymous=True)
        self.socket = None
        self.connected = False
        self.connect_socket()
        rospy.Subscriber("/scan", LaserScan, self.callback)
        rospy.loginfo("Lidar to socket node initialized.")
        rospy.spin()

    def connect_socket(self):
        while not rospy.is_shutdown():
            try:
                self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.socket.connect(SOCKET_PATH)
                self.connected = True
                rospy.loginfo("Connected to Unix socket: %s", SOCKET_PATH)
                break
            except socket.error as e:
                rospy.logwarn("Socket not ready yet, retrying in 2s... (%s)", e)
                time.sleep(2)

    def callback(self, scan):
        if not self.connected:
            return

        data = []
        angle = scan.angle_min
        for r in scan.ranges:
            if scan.range_min < r < min(scan.range_max, MAX_DISTANCE_TO_SEND):
                angle_deg = math.degrees(angle) % 360
                if ANGLE_MIN_DEG <= angle_deg <= ANGLE_MAX_DEG:
                    data.append({
                        'angle': round(angle_deg, 2),
                        'distance': round(r, 3)
                    })
            angle += scan.angle_increment

        if data:
            try:
                self.socket.sendall((json.dumps(data) + '\n').encode())
            except socket.error as e:
                rospy.logwarn("Lost socket connection: %s", e)
                self.connected = False
                self.socket.close()
                self.connect_socket()

if __name__ == '__main__':
    try:
        LidarToSocket()
    except rospy.ROSInterruptException:
        pass
