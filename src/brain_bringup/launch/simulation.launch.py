# Purpose: Launch Brain against the Gazebo simulator interface.
# Inputs: Simulator ROS topics and optional launch arguments.
# Outputs: Simulator-adapted autonomous Brain process.


from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='brain_io',
            executable='brain',
            name='brain',
            output='screen',
            arguments=['--mode', 'simulation'],
        ),
    ])