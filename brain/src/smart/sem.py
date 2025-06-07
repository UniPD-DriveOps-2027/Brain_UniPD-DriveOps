#!/usr/bin/env python3
import rospy
from utils.msg import semaphore  # replace 'utils.msg' with your actual package path

def main():
    rospy.init_node("simple_semaphore_antimaster_publisher")

    pub = rospy.Publisher("/automobile/trafficlight/antimaster", semaphore, queue_size=1)
    rospy.sleep(1)  # wait for connection

    msg = semaphore()
    msg.state = 2   # green
    msg.pos_x = 0.0
    msg.pos_y = 0.0

    rate = rospy.Rate(1)  # 1 Hz
    rospy.loginfo("Publishing GREEN to /automobile/trafficlight/antimaster")

    while not rospy.is_shutdown():
        pub.publish(msg)
        rospy.loginfo("Published state %d to antimaster semaphore", msg.state)
        rate.sleep()

if __name__ == "__main__":
    main()
