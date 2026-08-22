# Purpose: Launch Unix-socket dashboard output bridges.
# Inputs: ROS topic availability and socket parameters.
# Outputs: Camera, lidar, and metrics bridge node processes.


from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='brain_io', executable='camera_to_socket', output='screen'),
        Node(package='brain_io', executable='lidar_to_socket', output='screen'),
        Node(package='brain_io', executable='metrics_to_socket', output='screen'),
    ])