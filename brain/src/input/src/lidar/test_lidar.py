#!/usr/bin/python3
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

class LidarSteeringPI:
    def __init__(self):
        rospy.init_node('lidar_steering_pi_d')
        self.sub_lidar = rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
        self.pub_steering = rospy.Publisher("/automobile/command/steer", Float32, queue_size=1)
        #self.pub_speed = rospy.Publisher("/automobile/command/speed", Float32, queue_size=1)
        
        # Parameters
        self.desired_distance = 0.255  # Target distance from wall (meters)
        self.Kp = 200.0  # Proportional gain (degrees per meter)
        self.Ki = 0  # Integral gain (degrees per meter-second)
        self.steering_limit_deg = 20.0 
        self.integral_max = 5.0  # Anti-windup: max integral term (degrees)
        self.threshhold_distance = 0.4 #when reaing this distnace you ge  

        # State variables
        self.integral_sum = 0.0  # Integral accumulator
        self.last_time = None  # For calculating Δt

    def lidar_callback(self, data: LaserScan):
        """PI controller for steering angle."""
        # Get LiDAR measurement at 90°
        angles = np.linspace(data.angle_min, data.angle_max, len(data.ranges))
        angle_90_rad = np.deg2rad(90)
        idx_90 = np.argmin(np.abs(angles - angle_90_rad))
        distance_90 = data.ranges[idx_90]
        
        # Skip invalid measurements
        if np.isinf(distance_90) or distance_90 < data.range_min or distance_90 > data.range_max:
            return
        
        if distance_90 > self.threshhold_distance:
            self.pub_steering.publish(Float32(0))
            return
        # Calculate error
        error = self.desired_distance - distance_90
        
        # Calculate Δt (time since last callback)
        current_time = rospy.get_time()
        if self.last_time is None:
            self.last_time = current_time
            return
        dt = current_time - self.last_time
        self.last_time = current_time
        
        # Update integral term (with anti-windup)
        self.integral_sum += error * dt
        self.integral_sum = np.clip(self.integral_sum, -self.integral_max, self.integral_max)
        
        # Compute PI output (degrees)
        steering_angle_deg = (self.Kp * error) + (self.Ki * self.integral_sum)

        steering_angle_deg = - steering_angle_deg

        print(f"Distance at 90 degrees: {distance_90}")
        print(f"Error: {error}")
        print(f"Steering angle degrees: {steering_angle_deg}")
        
        # Clamp steering angle to ±25°
        steering_angle_deg = np.clip(
            steering_angle_deg,
            -self.steering_limit_deg,
            self.steering_limit_deg
        )
        
        # Publish steering command
        self.pub_steering.publish(Float32(steering_angle_deg))

if __name__ == '__main__':
    try:
        print(f"HEZZZZ")
        LidarSteeringPI()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass