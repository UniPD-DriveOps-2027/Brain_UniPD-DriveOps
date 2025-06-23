#!/usr/bin/env python

import rospy
from utils.msg import vehicles
import time

def publisher():
    pub = rospy.Publisher('/automobile/vehicles', vehicles, queue_size=10)
    rospy.init_node('vehicles_publisher', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    posA = 17.0
    posB = 1.0
    rotA = 0.0
    rotB = 0.0
    ID = 1  # example vehicle ID

    while not rospy.is_shutdown():
        msg = vehicles()
        msg.ID = ID
        msg.timestamp = rospy.get_time()  # or time.time() if you prefer system time
        msg.posA = posA
        msg.posB = posB
        msg.rotA = rotA
        msg.rotB = rotB

        pub.publish(msg)
        rospy.loginfo(f'Publishing: ID={msg.ID}, timestamp={msg.timestamp}, posA={msg.posA}, posB={msg.posB}, rotA={msg.rotA}, rotB={msg.rotB}')

        #posA += 0.5
        posB += 0.2
        rotA = 0
        rotB = 0

        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
