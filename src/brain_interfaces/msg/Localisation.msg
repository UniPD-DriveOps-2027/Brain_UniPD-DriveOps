# Purpose: Carry timestamped planar localisation and orientation components.
# Inputs: Timestamp, position pair, and rotation pair from a localisation source.
# Outputs: A typed ROS localisation observation for hardware/V2X integration.
float64 timestamp
float32 pos_a
float32 pos_b
float32 rot_a
float32 rot_b
