
# Remove the devel and build directories
rm -rf devel build

catkin_make --pkg utils

catkin_make

curr_wd=$(pwd) #get the current working directory
echo export GAZEBO_MODEL_PATH=\""$curr_wd/src/models_pkg:\$GAZEBO_MODEL_PATH"\" >> devel/setup.bash
echo export ROS_PACKAGE_PATH=\""$curr_wd/src:\$ROS_PACKAGE_PATH"\" >> devel/setup.bash
