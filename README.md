1. First, to build the simulator, run in the "cd bfmc_2025/simulator2024" directory:

catkin_make --pkg utils

catkin_make

2. Then, change the "simulator/devel/setup.bash" file to tell ROS where the project is located in your drive. The path should look like this if ran inside the docker container:

```bash
#!/usr/bin/env bash
# generated from catkin/cmake/templates/setup.bash.in

CATKIN_SHELL=bash

# source setup.sh from same directory as this file
_CATKIN_SETUP_DIR=$(builtin cd "`dirname "${BASH_SOURCE[0]}"`" > /dev/null && pwd)
. "$_CATKIN_SETUP_DIR/setup.sh"

#Add this path
export GAZEBO_MODEL_PATH="/root/catkin_ws/src/bfmc_2025/simulator_2024/src/models_pkg:$GAZEBO_MODEL_PATH"
export ROS_PACKAGE_PATH="/root/catkin_ws/src/bfmc_2025/simulator_2024/src:$ROS_PACKAGE_PATH"
```

3. Source the setup file and launch the gazebo simulator
```bash
source simulator_2024/devel/setup.bash
roslaunch sim_pkg map_2024.launch  
```
4. Finally, in another terminal launch the main_brain.py:

```bash
cd ../ws_2024/src/smart && python3 main_brain --sim
```

If the gui is not enabled, open a new terminal session, source devel/setup.bash and run gzclient
