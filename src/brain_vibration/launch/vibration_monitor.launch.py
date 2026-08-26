from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    config = PathJoinSubstitution([
        FindPackageShare('brain_vibration'),
        'config',
        'vibration.yaml',
    ])
    return LaunchDescription([
        Node(
            package='brain_vibration',
            executable='vibration_monitor',
            name='vibration_monitor',
            output='screen',
            parameters=[config],
        ),
    ])
