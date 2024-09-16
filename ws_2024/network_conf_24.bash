## S_H_net connection

# Master IP address
export ROS_MASTER_URI=http://192.168.0.101:1311

# Local computer IP Address
export ROS_HOSTNAME=192.168.0.101
export ROS_IP=192.168.0.101

echo "ROS_IP:           $ROS_IP"
echo "ROS_MASTER_URI:   $ROS_MASTER_URI"
echo "ROS_HOSTNAME:     $ROS_HOSTNAME"

# Where the setup.bash is
source /home/pi/bfmc2024/ws_2024/devel/setup.bash

