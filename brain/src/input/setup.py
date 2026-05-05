from setuptools import setup, find_packages

package_name = 'input'

_all_src = find_packages(where='src')
_flat = [p for p in _all_src if p != 'utils' and not p.startswith('utils.')]
_src_prefixed = ['src'] + ['src.' + p for p in _all_src]

setup(
    name=package_name,
    version='0.0.0',
    packages=_flat + _src_prefixed,
    package_dir={'': 'src', 'src': 'src'},
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
            'imuNODE           = imu.imuNODE:main',
            'semaphoreNODE     = semaphore.semaphoreNODE:main',
            'sonarNODE         = sonar.sonarNODE_2025:main',
            'gpstrackerNODE    = gpstracker.gpstrackerNODE:main',
            'trafficBridgeNODE  = data.trafficBridge:main',
            'semaphoreBridgeNODE = data.semaphoreBridge:main',
            # Un-comment as needed:
            # 'vehicletovehicleNODE = vehicletovehicle.vehicletovehicleNODE:main',
            # 'semaphoreNODE2025 = server.semaphoreNODE2025:main',
            # 'serverNODE2025    = server.serverNODE2025:main',
        ],
    },
)
