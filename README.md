<!-- Purpose: Provide setup, launch, operation, and safety instructions. Inputs: repository commands and runtime modes. Outputs: user-facing Brain usage guide. -->

# Brain_UniPD-DriveOps

Updated ROS 2 Jazzy brain and hardware stack for UniPD DriveOps BFMC.

This repository was rebuilt section by section from `Brain_DEI` around one
explicit runtime pipeline:

```text
AutomobileData interface
          |
          v
Detection + PathPlanning + state machine
          |
          v
Controllers
          |
          v
Vehicle commands + Unix socket outputs
```

The current simulator is maintained separately in
`~/BFMC_2027/Simulator_UniPD-DriveOps`.

## Structure

```text
src/
├── brain_interfaces/          Custom ROS 2 data formats shared between nodes
├── brain_core/
│   └── brain_core/
│       ├── vehicle_interface/ Car data plus commands such as drive, steer and stop
│       ├── perception/        Turns camera images into lanes, stop lines and signs
│       ├── planning/          Uses the track map to create a checkpoint route
│       ├── state_machine/     Decides what the car should do next
│       ├── controllers/       Calculates steering, speed and parking commands
│       ├── common/            Shared settings, maths and file-location helpers
│       └── assets/            Track maps, road data and trained AI model files
├── brain_io/
│   └── brain_io/
│       ├── adapters/          Converts hardware or simulator data to one car API
│       ├── inputs/            Reads IMU, sonar and vehicle/traffic-system messages
│       ├── outputs/           Sends camera, LiDAR and car status to the dashboard
│       └── runner.py          Selects a mode, connects the parts and starts Brain
└── brain_bringup/
    ├── launch/                Commands that start the required ROS 2 nodes together
    └── config/                Settings loaded by ROS 2 nodes when they start
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for ownership rules and topic contracts.

## Install dependencies

```bash
cd ~/BFMC_2027/Brain_UniPD-DriveOps
sudo rosdep init  # only if rosdep has not already been initialized
rosdep update
rosdep install --from-paths src --ignore-src -r -y
python3 -m pip install -r requirements.txt
```

Use a virtual environment or your platform's approved Python package workflow
if the system Python installation is externally managed.

## Build

```bash
cd ~/BFMC_2027/Brain_UniPD-DriveOps
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## Run with the updated simulator

Start `Simulator_UniPD-DriveOps` first. In a second terminal:

```bash
cd ~/BFMC_2027/Brain_UniPD-DriveOps
source /opt/ros/jazzy/setup.bash
source install/setup.bash
ros2 launch brain_bringup simulation.launch.py
```

The simulator adapter consumes `/oak/rgb/image_rect`, `/oak/imu/data`, encoder
and localisation topics, then sends JSON commands on `/automobile/command`.

### Checkpoint/path following

Normal autonomous steering follows the clothoid-interpolated graph path between
the configured checkpoints. A Pure Pursuit controller uses graph-frame
localisation and IMU yaw; the lane-following neural network is not used for
normal lane steering. Camera perception remains available for stop lines,
signs, pedestrians, and the existing specialised intersection behaviours.

The simulator adapter converts Gazebo localisation into the metric frame of
`final_graph.graphml`, selects the starting node from the live pose, and resets
path-tracking progress whenever a new checkpoint segment is generated. In
simulation, current 50 Hz encoder odometry supplies the controller pose while
the delayed/noisy GPS topic remains available for startup and compatibility.

To isolate checkpoint steering from camera detections and event transitions,
use the simulator-only test launch:

```bash
ros2 launch brain_bringup checkpoint_test.launch.py
```

This mode deliberately ignores stop lines, crosswalks, traffic, pedestrians,
obstacles, parking, tunnels, and intersection/roundabout manoeuvres. Use it only
in the simulator or on a closed test course. The normal
`simulation.launch.py` keeps the complete event state machine enabled.

## Run on the physical car

Review `src/brain_bringup/config/v2x.yaml`, especially `device_id`, before use.

```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash
ros2 launch brain_bringup hardware.launch.py
```

Optional launch switches:

```bash
ros2 launch brain_bringup hardware.launch.py sonar:=false v2x:=false
```

## Dashboard socket outputs

```bash
ros2 launch brain_bringup dashboard.launch.py
```

The receiving dashboard must create its Unix sockets before the output bridges
can connect.

## SPARCS/Vicon testing

Lap paths, track maps, the original SPARCS scripts, and a ROS 2 actual-coordinate
logger are kept separately under
[`testing/sparcs_vicon`](testing/sparcs_vicon/README.md). This testing material
is not installed with the production ROS packages.
