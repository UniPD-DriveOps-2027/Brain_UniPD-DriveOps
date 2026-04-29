"""
run_automobile.launch.py — ROS2 Jazzy replacement for run_automobile_2024.launch

Place this file at:   utils/launch/run_automobile.launch.py

Build and run:
    colcon build --symlink-install
    ros2 launch utils run_automobile.launch.py
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        # ── LiDAR ──────────────────────────────────────────────────────── #
        # Install: sudo apt install ros-jazzy-rplidar-ros
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            name='rplidarNode',
            parameters=[{
                'serial_port':      '/dev/ttyUSB0',
                'serial_baudrate':  115200,
                'frame_id':         'laser',
                'inverted':         False,
                'angle_compensate': True,
            }],
            output='screen',
        ),

        # ── micro-ROS agent (replaces rosserial_python) ────────────────── #
        # Install: sudo apt install ros-jazzy-micro-ros-agent
        # Flash micro-ROS firmware on the Nucleo/Arduino first.
        # Node(
        #     package='micro_ros_agent',
        #     executable='micro_ros_agent',
        #     name='micro_ros_agent',
        #     arguments=['serial', '--dev', '/dev/ttyACM0', '-b', '1000000'],
        #     output='screen',
        # ),

        # ── Input sensors ──────────────────────────────────────────────── #
        # Node(
        #     package='input',
        #     executable='imuNODE',
        #     name='imuNODE',
        #     output='screen',
        # ),
        # Node(
        #     package='input',
        #     executable='semaphoreNODE',
        #     name='semaphoreNODE',
        #     output='screen',
        # ),

        # ── Unix socket outputs ────────────────────────────────────────── #
        Node(
            package='unix_out',
            executable='metrics_to_socket',
            name='metrics_to_socket_NODE',
            output='screen',
        ),
        Node(
            package='unix_out',
            executable='lidar_to_socket',
            name='lidar_to_socket_NODE',
            output='screen',
        ),

        # ── Optionally enable other nodes ──────────────────────────────── #
        # Node(package='input',  executable='sonarNODE',         name='sonarNODE'),
        # Node(package='input',  executable='gpstrackerNODE',    name='gpstrackerNODE'),
        # Node(package='output', executable='serialNODE',        name='serialNODE'),
        # Node(package='output', executable='environmentalNODE', name='environmentalNODE'),
        # Node(package='input',  executable='vehicletovehicleNODE', name='vehicletovehicleNODE'),
    ])
