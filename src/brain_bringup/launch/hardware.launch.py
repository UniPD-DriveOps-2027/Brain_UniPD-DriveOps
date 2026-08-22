# Purpose: Launch Brain against the physical vehicle hardware stack.
# Inputs: ROS hardware topics, V2X configuration, and launch environment.
# Outputs: Hardware adapter, sensor/V2X nodes, and autonomous Brain process.


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('sonar', default_value='true'),
        DeclareLaunchArgument('v2x', default_value='true'),
        DeclareLaunchArgument(
            'v2x_config',
            default_value=PathJoinSubstitution([
                FindPackageShare('brain_bringup'), 'config', 'v2x.yaml'
            ]),
        ),
        Node(
            package='brain_core',
            executable='oak_camera',
            name='oak_camera',
            output='screen',
        ),
        Node(
            package='brain_io',
            executable='sonar',
            name='sonar',
            condition=IfCondition(LaunchConfiguration('sonar')),
            output='screen',
        ),
        Node(
            package='brain_io',
            executable='traffic_bridge',
            name='traffic_bridge',
            condition=IfCondition(LaunchConfiguration('v2x')),
            parameters=[LaunchConfiguration('v2x_config')],
            output='screen',
        ),
        Node(
            package='brain_io',
            executable='semaphore_bridge',
            name='semaphore_bridge',
            condition=IfCondition(LaunchConfiguration('v2x')),
            output='screen',
        ),
        Node(
            package='brain_io',
            executable='brain',
            name='brain',
            output='screen',
            arguments=['--mode', 'hardware'],
        ),
    ])