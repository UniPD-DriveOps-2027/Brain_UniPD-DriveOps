"""Run camera stabilization and vibration metrics without starting autonomous Brain."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='brain_vibration',
            executable='vibration_monitor',
            name='vibration_monitor',
            output='screen',
        ),
        Node(
            package='brain_camera',
            executable='image_stabilizer',
            name='oak_image_stabilizer',
            output='screen',
        ),
    ])
