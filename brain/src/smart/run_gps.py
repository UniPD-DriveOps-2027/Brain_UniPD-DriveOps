#!/usr/bin/env python3

import rospy
import numpy as np
import collections
from std_msgs.msg import Float32
from utils.msg import vehicles

class FixedGPSPublisher:
    def __init__(self):
        rospy.init_node('fixed_gps_override_node', anonymous=True)

        # Create a publisher to the same topic used by GPS
        self.pub = rospy.Publisher('/automobile/vehicles', vehicles, queue_size=1)

        # Fixed values to simulate GPS
        self.fixed_posA = 0.818  # Replace with desired posA (X in local system)
        self.fixed_posB = 2.28  # Replace with desired posB (Y in local system)

        self.rate = rospy.Rate(10)  # 10 Hz

    def run(self):
        rospy.loginfo("Fixed GPS Override Node Started. Publishing fixed GPS coordinates...")
        while not rospy.is_shutdown():
            msg = vehicles()
            msg.pos_a = self.fixed_posA
            msg.pos_b = self.fixed_posB
            rospy.loginfo(f"Publishing fixed GPS: posA = {msg.pos_a}, posB = {msg.pos_b}")
            self.pub.publish(msg)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        node = FixedGPSPublisher()
        node.run()
    except rospy.ROSInterruptException:
        pass
