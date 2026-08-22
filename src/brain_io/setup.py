# Purpose: Define setuptools metadata and ROS console entry points for this package.
# Inputs: Package source, manifests, resource files, and dependency metadata.
# Outputs: Installable Python package, assets, and executable entry points.


from setuptools import find_packages, setup


package_name = 'brain_io'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'brain_io': ['inputs/v2x/TrafficCommunication/useful/*.pem'],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    tests_require=['pytest'],
    zip_safe=False,
    maintainer='UniPD DriveOps',
    maintainer_email='driveops@unipd.it',
    description='ROS 2 adapters, sensor bridges, vehicle commands and dashboard outputs.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'brain = brain_io.runner:main',
            'imu = brain_io.inputs.imu:main',
            'sonar = brain_io.inputs.sonar:main',
            'traffic_bridge = brain_io.inputs.v2x.traffic_bridge:main',
            'semaphore_bridge = brain_io.inputs.v2x.semaphore_bridge:main',
            'camera_to_socket = brain_io.outputs.camera_to_socket:main',
            'lidar_to_socket = brain_io.outputs.lidar_to_socket:main',
            'metrics_to_socket = brain_io.outputs.metrics_to_socket:main',
        ],
    },
)