#!/usr/bin/env python3

import rospy
from utils.msg import semaphore
import numpy as np

class SemaphoreSimulator:
    def __init__(self):
        rospy.init_node('semaphore_simulator', anonymous=True)

        # Shared state machine for simplicity (can be changed per semaphore if needed)
        self.current_state = 0  # 0: RED, 1: YELLOW, 2: GREEN
        self.state_durations = [20, 3, 1.0]  # Duration for each state
        self.last_change_time = rospy.get_time()

        # Define all semaphore publishers and their positions
        self.semaphores = {
            "master":     {"pub": rospy.Publisher('/automobile/semaphore/master', semaphore, queue_size=5),
                           "position": np.array([3.19, 3.38])}, # 3.19, 3.38
            "slave":      {"pub": rospy.Publisher('/automobile/semaphore/slave', semaphore, queue_size=5),
                           "position": np.array([2.79, 4.93])},  # 2.79, 4.93
            "antimaster": {"pub": rospy.Publisher('/automobile/semaphore/antimaster', semaphore, queue_size=5),
                           "position": np.array([2.21, 3.96])},
            "antislave":  {"pub": rospy.Publisher('/automobile/semaphore/antislave', semaphore, queue_size=5),
                           "position": np.array([3.77, 4.36])},
            "start":      {"pub": rospy.Publisher('/automobile/semaphore/start', semaphore, queue_size=5),
                           "position": np.array([1.0, 1.0])}
        }

        self.rate = rospy.Rate(10)  # 10Hz

    def update_state(self):
        current_time = rospy.get_time()
        time_in_state = current_time - self.last_change_time
        if time_in_state > self.state_durations[self.current_state]:
            self.current_state = (self.current_state + 1) % 3
            self.last_change_time = current_time
            rospy.loginfo(f"[SemaphoreSimulator] State changed to: {self.get_state_name(self.current_state)}")

    def get_state_name(self, state):
        return {0: "RED", 1: "YELLOW", 2: "GREEN"}.get(state, "UNKNOWN")

    def publish_all(self):
        for name, sem_data in self.semaphores.items():
            msg = semaphore()
            msg.state = self.current_state
            msg.pos_x = sem_data["position"][0]
            msg.pos_y = sem_data["position"][1]
            sem_data["pub"].publish(msg)
            #rospy.loginfo(f"Published {self.get_state_name(msg.state)} to {name} at ({msg.pos_x}, {msg.pos_y})")

    def run(self):
        rospy.loginfo("Starting multi-semaphore simulator...")
        while not rospy.is_shutdown():
            self.update_state()
            self.publish_all()
            self.rate.sleep()


if __name__ == '__main__':
    try:
        simulator = SemaphoreSimulator()
        simulator.run()
    except rospy.ROSInterruptException:
        pass
