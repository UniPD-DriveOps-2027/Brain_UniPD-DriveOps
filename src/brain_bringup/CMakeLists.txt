# Purpose: Install Brain launch and configuration files as a ROS 2 ament package.
# Inputs: package metadata plus launch/ and config/ source directories.
# Outputs: Installed brain_bringup share directory.
cmake_minimum_required(VERSION 3.8)
project(brain_bringup)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
