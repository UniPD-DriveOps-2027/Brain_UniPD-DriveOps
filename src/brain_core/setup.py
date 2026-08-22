# Purpose: Define setuptools metadata and ROS console entry points for this package.
# Inputs: Package source, manifests, resource files, and dependency metadata.
# Outputs: Installable Python package, assets, and executable entry points.


from setuptools import find_packages, setup


package_name = 'brain_core'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'brain_core': [
            'assets/data/*',
            'assets/models/*',
            'assets/models/obstacle_models/*',
            'assets/models/traffic_signs_models/*',
        ],
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
    description='Vehicle interface, perception, planning, state machine and controllers.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'oak_camera = brain_core.perception.oak_camera:main',
        ],
    },
)