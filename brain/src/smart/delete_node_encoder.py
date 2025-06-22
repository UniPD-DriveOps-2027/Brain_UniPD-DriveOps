#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

if __name__ == '__main__':
    rospy.init_node('encoder_distance_simulator')
    pub = rospy.Publisher('/automobile/encoder/distance', Float32, queue_size=10)
    rate = rospy.Rate(1)  # 10 Hz

    value = 0.0
    increment = 0.02  # m

    while not rospy.is_shutdown():
        pub.publish(value)
        value += increment
        print(f"Encoder distance: {value}")
        rate.sleep()
