#!/usr/bin/env python

import rospy
from utils.msg import vehicles

def publisher():
    pub = rospy.Publisher('vehicles', vehicles, queue_size=10)
    rospy.init_node('vehicles_publisher', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    posA = 0.0
    posB = 0.0

    while not rospy.is_shutdown():
        msg = vehicles()
        msg.posA = posA
        msg.posB = posB

        pub.publish(msg)
        rospy.loginfo(f'Publishing: posA={msg.posA}, posB={msg.posB}')

        posA += 0.06
        posB += 0.05

        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
