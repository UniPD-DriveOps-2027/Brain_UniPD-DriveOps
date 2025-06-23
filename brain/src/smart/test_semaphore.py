#!/usr/bin/env python3

import rospy
from utils.msg import semaphore
import numpy as np

class SemaphoreSimulator:
    def __init__(self):
        rospy.init_node('semaphore_simulator', anonymous=True)
        
        # Semaphore parameters
        self.semaphore_position = np.array([5.0, 4.0])  # x=5, y=4
        self.current_state = 0  # 0: RED, 1: YELLOW, 2: GREEN
        self.state_durations = [1.0, 1.0, 10.0]  # Duration for each state (RED, YELLOW, GREEN)
        self.last_change_time = rospy.get_time()
        
        # Create publisher
        self.pub = rospy.Publisher('/automobile/semaphore/antimaster', semaphore, queue_size=5)
        
        # Set publish rate
        self.rate = rospy.Rate(10)  # 10Hz
        
    def update_state(self):
        current_time = rospy.get_time()
        time_in_state = current_time - self.last_change_time
        
        # Check if we need to change state
        if time_in_state > self.state_durations[self.current_state]:
            self.current_state = (self.current_state + 1) % 3
            self.last_change_time = current_time
            rospy.loginfo(f"Semaphore state changed to: {self.get_state_name(self.current_state)}")
    
    def get_state_name(self, state):
        states = {0: "RED", 1: "YELLOW", 2: "GREEN"}
        return states.get(state, "UNKNOWN")
    
    def publish_semaphore(self):
        msg = semaphore()
        msg.state = self.current_state
        msg.pos_x = self.semaphore_position[0]
        msg.pos_y = self.semaphore_position[1]
        self.pub.publish(msg)
    
    def run(self):
        rospy.loginfo(f"Starting semaphore simulator at position (x={self.semaphore_position[0]}, y={self.semaphore_position[1]})")
        while not rospy.is_shutdown():
            self.update_state()
            self.publish_semaphore()
            self.rate.sleep()

if __name__ == '__main__':
    try:
        simulator = SemaphoreSimulator()
        simulator.run()
    except rospy.ROSInterruptException:
        pass