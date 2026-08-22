# Purpose: Carry traffic-light state and mapped planar position.
# Inputs: Semaphore state plus graph-frame x/y coordinates.
# Outputs: A typed ROS semaphore observation consumed by the environment state.
uint8 state
float32 pos_x
float32 pos_y
