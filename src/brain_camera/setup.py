from glob import glob
from setuptools import find_packages, setup


package_name = 'brain_camera'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', glob('config/*.yaml')),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    tests_require=['pytest'],
    zip_safe=False,
    maintainer='UniPD DriveOps',
    maintainer_email='driveops@unipd.it',
    description='Partially stabilizes the OAK RGB stream using vehicle IMU motion.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'image_stabilizer = brain_camera.image_stabilizer:main',
        ],
    },
)
