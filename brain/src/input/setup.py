from setuptools import setup, find_packages

package_name = 'input'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    data_files=[
        # Required for ament resource index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='BFMC',
    maintainer_email='futuremobilitychallenge@bosch.com',
    description='Sensor nodes: IMU, GPS, sonar, semaphore',
    license='BSD-3',
    # Maps CLI executable names to Python entry points
    entry_points={
        'console_scripts': [
            'imuNODE         = imu.imuNODE:main',
            'semaphoreNODE   = semaphore.semaphoreNODE:main',
            'sonarNODE       = sonar.sonarNODE_2025:main',
            'gpstrackerNODE  = gpstracker.gpstrackerNODE:main',
            # Un-comment as needed:
            # 'vehicletovehicleNODE = vehicletovehicle.vehicletovehicleNODE:main',
            # 'semaphoreNODE2025 = server.semaphoreNODE2025:main',
            # 'serverNODE2025    = server.serverNODE2025:main',
        ],
    },
)
