#!/usr/bin/env python3
# Purpose: Read ultrasonic range sensors and publish ROS 2 distances.
# Inputs: GPIO echo/trigger signals and sensor configuration.
# Outputs: Range measurements on automobile sonar topics.

"""
sonarNODE — ROS2 Jazzy version
HC-SR04 ultrasonic sensor node using GPIO.
"""

import sys
import time
import threading

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

try:
    import RPi.GPIO as gpio
except ImportError:
    gpio = None  # allow import on non-Pi for testing


class SonarNode(Node):
    def __init__(self):
        super().__init__('sonarNODE')

        self.sonars_n = 3
        self.publishers = [
            self.create_publisher(Float32, '/automobile/sonar/center', 1),
            self.create_publisher(Float32, '/automobile/sonar/right',  1),
            self.create_publisher(Float32, '/automobile/sonar/left',   1),
        ]
        self.sampling_time   = 0.06
        self.max_fly_time    = 0.02

        self._init_sonar()

        self._thread = threading.Thread(target=self._getting, daemon=True)
        self._thread.start()
        self.get_logger().info("sonarNODE started")

    def _init_sonar(self):
        if gpio is None:
            self.get_logger().warn("RPi.GPIO not available — sonar disabled")
            return
        gpio.setmode(gpio.BCM)
        self.trig_center = 23
        self.trig_right  = 20
        self.trig_left   = 27
        self.echos       = [24, 21, 22]

        gpio.setup(self.trig_center, gpio.OUT)
        gpio.setup(self.trig_right,  gpio.OUT)
        gpio.setup(self.trig_left,   gpio.OUT)
        for e in self.echos:
            gpio.setup(e, gpio.IN)

    def _getting(self):
        if gpio is None:
            return

        gpio.output(self.trig_center, False)
        gpio.output(self.trig_right,  False)
        gpio.output(self.trig_left,   False)
        time.sleep(0.5)

        while rclpy.ok():
            gpio.output(self.trig_center, True)
            gpio.output(self.trig_right,  True)
            gpio.output(self.trig_left,   True)
            time.sleep(0.00001)
            gpio.output(self.trig_center, False)
            gpio.output(self.trig_right,  False)
            gpio.output(self.trig_left,   False)

            echo_flags  = [False] * self.sonars_n
            done_flags  = [False] * self.sonars_n
            distances   = [3.0]   * self.sonars_n
            start_times = [time.time()] * self.sonars_n
            t0 = time.time()

            while time.time() - t0 < self.max_fly_time and not all(done_flags):
                now = time.time()
                for i in range(self.sonars_n):
                    if gpio.input(self.echos[i]) == 1 and not echo_flags[i]:
                        echo_flags[i]  = True
                        start_times[i] = now
                    if gpio.input(self.echos[i]) == 0 and echo_flags[i] and not done_flags[i]:
                        distances[i]  = (now - start_times[i]) * 343.0 / 2
                        done_flags[i] = True

            for i in range(self.sonars_n):
                val = distances[i] if echo_flags[i] else -2.0
                self.publishers[i].publish(Float32(data=float(val)))

            time.sleep(self.sampling_time)

    def destroy_node(self):
        if gpio:
            gpio.cleanup()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SonarNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
