# Purpose: Carry high-level road and manoeuvre conditions.
# Inputs: Boolean condition values produced by environment/decision logic.
# Outputs: A typed ROS message consumed by Brain behaviours and bridges.
bool can_overtake
bool highway
bool car_on_path
bool rerouting
bool tunnel
