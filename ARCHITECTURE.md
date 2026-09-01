<!-- Purpose: Explain Brain component ownership and dependency flow. Inputs: current repository structure and runtime contracts. Outputs: architecture guidance for maintainers. -->

# Architecture

## Dependency direction

Dependencies flow in one direction:

```text
brain_interfaces <- brain_core <- brain_io <- brain_bringup
```

- `brain_interfaces` defines transport-neutral shared message schemas.
- `brain_core` contains driving decisions and never selects hardware.
- `brain_io` translates ROS topics, hardware and simulator data into the core
  vehicle API and translates commands back out.
- `brain_bringup` chooses and configures the executable composition.

## 1. AutomobileData interface

`brain_core.vehicle_interface.Automobile_Data` owns the shared vehicle state
and command contract. The state machine knows only this API:

```python
car.drive(speed, angle)
car.drive_speed(speed)
car.drive_angle(angle)
car.drive_distance(distance)
car.stop(angle)
```

Concrete transport implementations are outside core:

- `brain_io.adapters.hardware.AutomobileDataPi`
- `brain_io.adapters.simulator.AutomobileDataSimulator`

Both normalize external units into metres, seconds and radians.

## 2. Detection, planning and state machine

- `perception/detection.py`: lane, intersection, stop-line, sign and obstacle
  inference copied from the active Brain_DEI implementation.
- `perception/oak_camera.py`: physical OAK-D acquisition and traffic-sign node.
- `planning/path_planner.py`: graph loading, route generation and navigation.
- `state_machine/autonomous.py`: competition behaviour state machine.
- `state_machine/remote.py`: optional manual/RC behaviour.
- `state_machine/environment.py`: vehicle, obstacle and semaphore state.

Runtime assets are resolved from the installed Python package; execution no
longer depends on the terminal's current working directory. Writable resume
and log state goes under `~/.local/state/brain_unipd_driveops` by default. Set
`BRAIN_STATE_DIR` to override it.

## 3. Controllers

- `controllers/steering.py`: lateral/yaw controller.
- `controllers/speed.py`: desired and curve-speed selection.
- `controllers/parking.py`: precise parking manoeuvres.

Controllers return decisions through the injected AutomobileData object. They
do not publish directly to ROS topics.

## 4. Commands and outputs

The hardware adapter publishes split hardware command topics. The simulator
adapter converts the same API to the simulator's JSON action messages.

Dashboard adapters observe ROS state independently:

- `outputs/camera_to_socket.py`
- `outputs/lidar_to_socket.py`
- `outputs/metrics_to_socket.py`

They are outputs only and do not feed decisions back into the state machine.

## Simulator topic contract

| Topic | Type | Direction |
|---|---|---|
| `/oak/rgb/image_rect` | `sensor_msgs/Image` | simulator -> brain |
| `/automobile/imu/data` | `sensor_msgs/Imu` | simulator chassis IMU -> brain |
| `/automobile/encoder/speed` | `std_msgs/Float32` | simulator -> brain |
| `/automobile/encoder/distance` | `std_msgs/Float32` | simulator -> brain |
| `/automobile/localisation` | `std_msgs/String` JSON | simulator -> brain |
| `/automobile/command` | `std_msgs/String` JSON | brain -> simulator |

## Deliberately excluded legacy material

- ROS 1 simulator and `rospy` adapters
- Catkin workspace files
- Generated `build`, `install` and `log` trees
- Qualification videos and project-status documents
- Training notebooks and source ZIP archives
- Superseded planners, duplicate brain versions and manual test scripts
- Unused rosserial messages and services

## Test-only SPARCS/Vicon material

`testing/sparcs_vicon` is outside the ROS workspace by design. It preserves the
original lap paths and scripts and provides a ROS 2 logger for ground-truth
X/Y/yaw measurement. Production packages must not import from this directory.
