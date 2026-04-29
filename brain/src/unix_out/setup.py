# unix_out/setup.py
from setuptools import setup

package_name = 'unix_out'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=['lidar_to_socket', 'metrics_to_socket'],  # ← standalone .py files
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={'console_scripts': [
        'lidar_to_socket   = lidar_to_socket:main',
        'metrics_to_socket = metrics_to_socket:main',
    ]},
)