# Purpose: Launch Brain in simulator checkpoint-only path-following mode.
# Inputs: ROS environment and optional launch arguments.
# Outputs: brain_io runner process with simulation and path-only enabled.


"""Run graph checkpoint following with all event behaviours disabled."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='brain_io',
            executable='brain',
            name='brain_checkpoint_test',
            output='screen',
            arguments=['--mode', 'simulation', '--path-only'],
        ),
    ])