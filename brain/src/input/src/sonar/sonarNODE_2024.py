#!/usr/bin/env python3

import gpiod
import time
import sys
import rospy
from std_msgs.msg import Float32


class sonarNODE():
    def __init__(self):
        rospy.init_node('sonarNODE', anonymous=True)
        self.sonars_n = 3
        self.publishers = [rospy.Publisher('/automobile/sonar/center', Float32, queue_size=1),
                           rospy.Publisher('/automobile/sonar/right', Float32, queue_size=1),
                           rospy.Publisher('/automobile/sonar/left', Float32, queue_size=1)]

        # self.r = rospy.Rate(15)
        self.sampling_time = 0.06  # 1/20.0
        self.max_train_pulse_time = 0.01
        self.max_fly_time = 0.01 * 2

    def run(self):
        rospy.loginfo("starting sonarNODE")
        self._initSONAR()
        self._getting()

    def _initSONAR(self):
        # Configure the chip and lines for trig and echo pins
        self.chip = gpiod.Chip('gpiochip0')  # Adjust gpiochip as needed
        self.trig_center = self.chip.get_line(5)
        self.trig_right = self.chip.get_line(23)  # 5
        self.trig_left = self.chip.get_line(27)

        self.echos = [self.chip.get_line(6), self.chip.get_line(24), self.chip.get_line(22)]  # BFMC_2024 #21 was 6

        # Request lines for trig and echo
        self.trig_center.request(consumer="TRIG", type=gpiod.LINE_REQ_DIR_OUT)
        self.trig_right.request(consumer="TRIG", type=gpiod.LINE_REQ_DIR_OUT)
        self.trig_left.request(consumer="TRIG", type=gpiod.LINE_REQ_DIR_OUT)

        for echo in self.echos:
            echo.request(consumer="ECHO", type=gpiod.LINE_REQ_DIR_IN)

        print("SONAR Name: HC-SR04")

    def _getting(self):
        # Set the trigger pins to low initially
        self.trig_center.set_value(0)
        self.trig_right.set_value(0)
        self.trig_left.set_value(0)
        time.sleep(0.5)

        while not rospy.is_shutdown():
            # Send the impulse
            self.trig_center.set_value(1)
            self.trig_right.set_value(1)
            self.trig_left.set_value(1)
            time.sleep(0.00001)  # impulse duration to 10us
            self.trig_center.set_value(0)
            self.trig_right.set_value(0)
            self.trig_left.set_value(0)

            echo_flags = [False] * self.sonars_n
            done_flags = [False] * self.sonars_n
            distances = [3.0] * self.sonars_n

            # wait for the comeback impulse
            start_time = time.time()
            curr_time = start_time
            start_sonar_times = [start_time] * self.sonars_n
            while curr_time - start_time < self.max_fly_time and not all(done_flags):
                curr_time = time.time()
                for i in range(self.sonars_n):
                    if self.echos[i].get_value() == 1 and not echo_flags[i]:
                        echo_flags[i] = True
                        start_sonar_times[i] = curr_time
                for i in range(self.sonars_n):
                    if self.echos[i].get_value() == 0 and echo_flags[i] and not done_flags[i]:
                        pulse_duration = curr_time - start_sonar_times[i]
                        distances[i] = pulse_duration * 343.0 / 2
                        done_flags[i] = True

            for i in range(self.sonars_n):
                if echo_flags[i]:
                    self.publishers[i].publish(distances[i])
                else:
                    self.publishers[i].publish(-2)

            time.sleep(self.sampling_time)


if __name__ == "__main__":
    try:
        sonarNod = sonarNODE()
        sonarNod.run()
    except (KeyboardInterrupt, SystemExit):
        print("Exception from KeyboardInterrupt or SystemExit")
        # Release the GPIO lines
        sonarNod.chip.release()
        sys.exit(0)
    except Exception as e:
        print('Finally *************++')
        print(e)
        # Release the GPIO lines
        sonarNod.chip.release()
        sys.exit(0)

