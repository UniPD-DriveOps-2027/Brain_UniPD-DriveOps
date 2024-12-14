#!/usr/bin/env bash
# generated from catkin/cmake/templates/setup.bash.in

#export GAZEBO_MODEL_PATH="/home/matheus/BFMC2024/Code/bfmc2024/pi_2024/simulator_2024/src/models_pkg:$GAZEBO_MODEL_PATH"
#export ROS_PACKAGE_PATH="/home/matheus/BFMC2024/Code/bfmc2024/pi_2024/simulator_2024/src:$ROS_PACKAGE_PATH"
export GAZEBO_MODEL_PATH="/home/eugen/catkin_ws/src/simulator_2024/simulator_2024/src/models_pkg:$GAZEBO_MODEL_PATH"
export ROS_PACKAGE_PATH="/home/eugen/catkin_ws/src/simulator_2024/simulator_2024/src:$ROS_PACKAGE_PATH"

CATKIN_SHELL=bash

# source setup.sh from same directory as this file
_CATKIN_SETUP_DIR=$(builtin cd "`dirname "${BASH_SOURCE[0]}"`" > /dev/null && pwd)
. "$_CATKIN_SETUP_DIR/setup.sh"
