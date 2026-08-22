<!-- Purpose: Record how legacy Brain_DEI components map into this ROS 2 repository. Inputs: old/new file ownership decisions. Outputs: migration and cleanup reference for maintainers. -->

# Brain_DEI migration map

| Brain_DEI source | New owner |
|---|---|
| `automobile_data_interface.py` | `brain_core/vehicle_interface/automobile_data.py` |
| `automobile_data_pi.py` | `brain_io/adapters/hardware.py` |
| `automobile_data_simulator.py` | Replaced by ROS 2 `brain_io/adapters/simulator.py` |
| `detection.py`, `stopline.py` | `brain_core/perception/` |
| `oak_camera_node.py` | `brain_core/perception/oak_camera.py` |
| `path_planning4_mod.py` | `brain_core/planning/path_planner.py` |
| `brain.py`, `rc_brain.py` | `brain_core/state_machine/` |
| `environmental_data_simulator.py` | `brain_core/state_machine/environment.py` |
| `controller3.py`, `controllerSP.py`, `parkman.py` | `brain_core/controllers/` |
| `input` ROS 2 nodes | `brain_io/inputs/` |
| `unix_out` nodes | `brain_io/outputs/` |
| `utils/msg` | `brain_interfaces/msg` |

The migration intentionally does not copy generated artifacts, ROS 1 nodes,
training experiments, duplicate implementations, or inactive model variants.
