from setuptools import setup, find_packages
package_name = 'output'
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={'console_scripts': [
        # left empty — serialNODE replaced by micro-ROS
        # environmentalNODE to be added when new competition code is ready
    ]},
)