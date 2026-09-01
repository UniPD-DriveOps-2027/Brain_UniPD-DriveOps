# Purpose: Launch Brain against the Gazebo simulator interface.
# Inputs: Simulator ROS topics and optional launch arguments.
# Outputs: Simulator-adapted autonomous Brain process.


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'localization_source',
            default_value='fused',
            description='Tracking source: fused (/odometry/global) or simulator (/automobile/localisation).',
        ),
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
        Node(
            package='brain_io',
            executable='brain',
            name='brain',
            output='screen',
            arguments=[
                '--mode', 'simulation',
                '--localization-source', LaunchConfiguration('localization_source'),
            ],
        ),
    ])
