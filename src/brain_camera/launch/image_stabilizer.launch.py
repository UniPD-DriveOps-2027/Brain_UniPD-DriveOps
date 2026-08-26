from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    config = PathJoinSubstitution([
        FindPackageShare('brain_camera'),
        'config',
        'stabilizer.yaml',
    ])
    return LaunchDescription([
        Node(
            package='brain_camera',
            executable='image_stabilizer',
            name='oak_image_stabilizer',
            output='screen',
            parameters=[config],
        ),
    ])
