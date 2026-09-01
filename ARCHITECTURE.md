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

## Package map

The ROS 2 packages under `src/` have these responsibilities:

| Package | Responsibility | Important entry points |
|---|---|---|
| `brain_interfaces` | Shared ROS message definitions. It contains transport/data schemas such as `Localisation`, `Conditions`, `Environmental`, `Vehicles`, and `Semaphore`; it contains no driving algorithm. | `src/brain_interfaces/msg/` |
| `brain_core` | The vehicle-independent autonomous algorithms: perception, map/path planning, controllers, vehicle-state contract, and competition state machine. It decides what the vehicle should do, but does not choose hardware or publish hardware-specific commands. | `brain_core.state_machine.autonomous:Brain`; `brain_core.planning.path_planner:PathPlanning`; `brain_core.controllers/` |
| `brain_io` | The ROS integration boundary. It reads sensors/localisation, adapts hardware or simulator data to the `Automobile_Data` API, and converts `drive()` decisions into vehicle commands. It also contains V2X inputs and dashboard socket outputs. | `brain_io.runner:main`; `adapters/hardware.py`; `adapters/simulator.py` |
| `brain_camera` | Camera conditioning. It uses IMU roll/pitch to stabilize and crop the RGB image and republishes corrected camera info and stabilization metadata. | `brain_camera.image_stabilizer:main`; `launch/image_stabilizer.launch.py` |
| `brain_vibration` | IMU diagnostics. It applies an exponential RMS estimator to linear acceleration and angular velocity and publishes vibration metrics. It does not control the vehicle. | `brain_vibration.vibration_monitor:main`; `launch/vibration_monitor.launch.py` |
| `brain_bringup` | Runtime composition. Its launch files start the required nodes for hardware, simulation, sensor conditioning, checkpoint tests, and dashboard output. | `launch/hardware.launch.py`; `launch/simulation.launch.py` |

## Main autonomous stack

The normal autonomous execution path is:

```text
brain_bringup/{hardware,simulation}.launch.py
        |
        v
brain_io.runner:main  (`brain` node)
        |
        +--> AutomobileDataPi       [hardware]
        |    or AutomobileDataSimulator [simulation]
        |          |
        |          +--> sensors/localisation -> Automobile_Data state
        |          +--> Automobile_Data commands -> hardware/simulator
        |
        +--> PathPlanning                 map graph and route
        +--> CheckpointFollower            route progress/lookahead
        +--> Detection                     signs, obstacles, stop lines, events
        +--> OpenCVLaneCenter              local lane-centre correction
        +--> Controller / ControllerSpeed  steering and speed decisions
        +--> Brain                         event/competition state machine
```

The composition root is `src/brain_io/brain_io/runner.py`. It constructs the
adapter, loads the map and models, creates the planner/controllers/perception,
then instantiates `src/brain_core/brain_core/state_machine/autonomous.py`.
`Brain.run()` is the main autonomous control loop. The core path is therefore
not a single executable inside `brain_core`; it is assembled by the `brain`
entry point in `brain_io` using classes from `brain_core`.

Supporting nodes launched alongside the autonomous process are:

- `brain_camera/image_stabilizer`: camera conditioning only; it does not make
  steering decisions.
- `brain_core/oak_camera`: physical OAK-D RGB acquisition and traffic-sign
  publishing on hardware runs.
- `brain_vibration/vibration_monitor`: publishes
  `/automobile/vibration/linear_acceleration_rms` and
  `/automobile/vibration/angular_velocity_rms` from `/automobile/imu/data`.
- `brain_io/sonar`, `traffic_bridge`, and `semaphore_bridge`: optional sensor
  and V2X inputs used by the environment/state machine.

`hardware.launch.py` starts the complete hardware composition. On simulation,
`simulation.launch.py` starts the simulator adapter, camera stabilizer, and
vibration monitor; the simulator itself supplies the camera and vehicle sensor
topics. `sensor_conditioning.launch.py` starts only the camera and vibration
support nodes, without autonomous driving.

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
