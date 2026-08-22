# Purpose: Carry another vehicle's identity, timestamp, pose, and rotation.
# Inputs: V2X vehicle ID and localisation fields.
# Outputs: A typed ROS neighbouring-vehicle observation.
uint8 id
float32 timestamp
float32 pos_a
float32 pos_b
float32 rot_a
float32 rot_b
