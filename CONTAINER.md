# Brain container

The Brain image owns the physical vehicle-facing Brain process and the OAK-D
camera. `brain_bringup hardware.launch.py` starts `brain_core/oak_camera` in
the same container as the autonomous Brain node, so the camera is not started
by Localization or Isaac ROS.

## Build once

From this repository:

```bash
./docker/build.sh
```

The image contains ROS 2 Jazzy, this workspace, the ONNX models, DepthAI, and
the Python runtime dependencies. The build is cached by Docker; normal runs
do not reinstall packages.

## Run

```bash
./docker/run.sh --normal-start
./docker/run.sh --random-start
```

The container uses host networking so all three containers share one ROS 2
graph. `--privileged` is used here because the Brain launch accesses OAK/GPIO
hardware. Stop it with `Ctrl-C`.

Published camera topics consumed by the other containers include:

```text
/oak/left/image_raw       sensor_msgs/Image (mono8)
/oak/right/image_raw      sensor_msgs/Image (mono8)
/oak/left/camera_info     sensor_msgs/CameraInfo
/oak/right/camera_info    sensor_msgs/CameraInfo
/oak/rgb/image_raw        sensor_msgs/Image (bgr8)
/oak/rgb/camera_info      sensor_msgs/CameraInfo
/traffic/detection        std_msgs/String
```

The vehicle firmware/bridge topics remain external inputs to the Brain and
Localization ROS graph.
