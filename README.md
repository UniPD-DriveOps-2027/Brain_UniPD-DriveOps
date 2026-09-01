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
├── brain_interfaces/          Shared ROS 2 messages
├── brain_core/
│   └── brain_core/
│       ├── vehicle_interface/ Common AutomobileData state and API
│       ├── perception/        Lane, stop-line and OAK-D perception
│       ├── planning/          Track graph and path planning
│       ├── state_machine/     Autonomous, RC and environment behaviour
│       ├── controllers/       Steering, speed and parking controllers
│       ├── common/            Constants, geometry and resource paths
│       └── assets/            Runtime maps and inference models
├── brain_io/
│   └── brain_io/
│       ├── adapters/          Hardware and ROS 2 simulator adapters
│       ├── inputs/            IMU, sonar and V2X bridges
│       ├── outputs/           Camera, LiDAR and metrics socket bridges
│       └── runner.py          Application composition root
└── brain_bringup/
    ├── launch/                Hardware, simulation and dashboard launchers
    └── config/                Runtime ROS parameters
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

## Complete hardware-free simulator test

Run the three components in separate terminals. No physical encoder, GPS,
IMU, camera, or localization hardware is required.

### Terminal 1: simulator and hardware-topic mapping

```bash
cd ~/BFMC_2027/Simulator_UniPD-DriveOps
source /opt/ros/jazzy/setup.bash
colcon build --packages-select sim2real_mapping sim_pkg --symlink-install
source install/setup.bash
ros2 launch sim_pkg map_with_car.launch camera_view:=false
```

This starts Gazebo, the bridges, simulated sensors, and `sim2real_mapping`.
The adapter publishes the hardware-compatible encoder, GPS JSON, IMU, and
camera topics. GPS/tag data uses a 2-second artificial delay by default.

### Terminal 2: localization stack

Build the localization image once:

```bash
cd ~/BFMC_2027/Localization_UniPD-DriveOps
./docker/build.sh
```

Then start it while the simulator remains running:

```bash
./docker/run.sh --normal-start
```

If it reports `Localization image is missing`, run `./docker/build.sh` first.

### Terminal 3: Brain

Build and source Brain:

```bash
cd ~/BFMC_2027/Brain_UniPD-DriveOps
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source ~/BFMC_2027/Simulator_UniPD-DriveOps/install/setup.bash
source install/setup.bash
```

Launch the Brain simulator mode:

```bash
ros2 launch brain_bringup simulation.launch.py
```

Select which localization source Brain uses for simulation tracking:

```bash
# UniPD fused localization (default): /odometry/global
ros2 launch brain_bringup simulation.launch.py localization_source:=fused

# Simulator reference localization: /automobile/localisation
ros2 launch brain_bringup simulation.launch.py localization_source:=simulator
```

With `fused`, Brain uses the pose and heading from `/odometry/global`. With
`simulator`, Brain uses the simulator's `/automobile/localisation` position
and simulator IMU heading. The unselected source is ignored for tracking.

For isolated checkpoint/path following:

```bash
ros2 launch brain_bringup checkpoint_test.launch.py
```

There is no `lane_following.launch.py` in `brain_bringup`. Normal simulator
steering is launched by `simulation.launch.py`; the checkpoint-only mode is
`checkpoint_test.launch.py`.

Verify the shared graph with:

```bash
ros2 topic list | grep -E \
'automobile/(command|encoder|imu|localisation)|odometry/(local|global)|oak/rgb'
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
