#!/usr/bin/env python3

import rospy
from utils.msg import IMU
import mmap
import time

# Define shared memory file
shm_file = "/dev/shm/imu_shared_memory"

YAW_OFFSET = 0.0  # Change this value to your desired offset

def apply_yaw_offset(yaw_value, offset):
    """
    Apply offset to yaw value and ensure it stays within 0-360 range
    Returns:
        float: Adjusted yaw value within 0-360 range
    """
    adjusted_yaw = yaw_value + offset
    
    # Normalize to 0-360 range
    while adjusted_yaw < 0:
        adjusted_yaw += 360.0
    while adjusted_yaw >= 360:
        adjusted_yaw -= 360.0
    
    return adjusted_yaw

# Function to parse the data from the shared memory
def parse_data(data_str):
    try:
        # Split the data string by commas and convert each part to float
        parts = [float(x) for x in data_str.strip().split(',')]
        if len(parts) != 9:
            rospy.logwarn(f"Invalid data length: Expected 9 values, got {len(parts)}")
            return None
        return parts
    except Exception as e:
        #rospy.logwarn(f"Error parsing IMU data: {e}")
        return None

# Main function to read from shared memory and publish to ROS topic
def main():
    rospy.init_node('imu_shared_memory_publisher', anonymous=True)
    pub = rospy.Publisher('/automobile/imu', IMU, queue_size=10)

    # Open shared memory
    with open(shm_file, "r") as f:
        shm = mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)

        rate = rospy.Rate(10)  # 10 Hz publishing rate

        while not rospy.is_shutdown():
            # Read data from shared memory
            shm.seek(0)
            raw = shm.read(1024).decode('utf-8', errors='ignore').split('\x00', 1)[0].strip()

            # Log raw data for debugging (Optional)
            rospy.logdebug(f"Raw data string: '{raw}'")

            # Parse the data
            values = parse_data(raw)
            if values:
                # Create the IMU message and assign values
                imu_msg = IMU()
                imu_msg.roll = values[0]
                imu_msg.pitch = values[1]

                original_yaw = values[2]
                imu_msg.yaw = apply_yaw_offset(original_yaw, YAW_OFFSET)

                imu_msg.accelx = values[3]
                imu_msg.accely = values[4]
                imu_msg.accelz = values[5]
                imu_msg.gyrox = values[6]
                imu_msg.gyroy = values[7]
                imu_msg.gyroz = values[8]
                
                # Publish the message to the ROS topic
                pub.publish(imu_msg)

            rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
