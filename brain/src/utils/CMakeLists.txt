cmake_minimum_required(VERSION 3.8)
project(utils)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

# Generate all custom messages and services
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/IMU.msg"
  "msg/Localisation.msg"
  "msg/Vehicles.msg"
  "msg/Environmental.msg"
  "msg/Log.msg"
  "msg/TopicInfo.msg"
  "msg/Semaphore.msg"
  "msg/Conditions.msg"
  "msg/Trafficsignprediction.msg"
  "srv/Subscribing.srv"
  "srv/RequestParam.srv"
  DEPENDENCIES std_msgs
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
