# Purpose: Generate shared ROS 2 message interfaces.
# Inputs: Message definition files and rosidl dependencies.
# Outputs: Language/type-support code for brain_interfaces messages.
cmake_minimum_required(VERSION 3.8)
project(brain_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Conditions.msg"
  "msg/Environmental.msg"
  "msg/Localisation.msg"
  "msg/Semaphore.msg"
  "msg/Vehicles.msg"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
