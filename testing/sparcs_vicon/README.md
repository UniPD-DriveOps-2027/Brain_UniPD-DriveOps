<!-- Purpose: Explain isolated SPARCS/Vicon coordinate testing tools. Inputs: test-tool layout and usage. Outputs: user-facing instructions that remain separate from production ROS packages. -->

# SPARCS and Vicon testing

This folder is deliberately separate from the production ROS packages. It
contains lap paths, map images and Vicon tools for collecting actual X/Y/yaw
coordinates on the SPARCS track.

## ROS 2 actual-coordinate logger

The maintained Jazzy tool subscribes to the Vicon rigid-body transform and
writes both raw and offset-corrected positions to CSV:

```bash
cd ~/BFMC_2027/Brain_UniPD-DriveOps/testing/sparcs_vicon
source /opt/ros/jazzy/setup.bash
python3 vicon_xy_logger.py \
  --topic /vicon/bfmc_car/bfmc_car \
  --output measurements/vicon_xy.csv
```

Default coordinate calibration copied from the original SPARCS test:

```text
x_world = x_vicon - (-1.3425)
y_world = y_vicon - (-2.35)
yaw_offset = -90 degrees
```

Override those values when recalibrating:

```bash
python3 vicon_xy_logger.py --x0 -1.3425 --y0 -2.35 \
  --yaw-offset-deg -90
```

To count laps at the original Y threshold and stop after three laps:

```bash
python3 vicon_xy_logger.py --lap-y 2.54 --laps 3
```

CSV columns include ROS timestamp, corrected X/Y/Z, yaw in radians and degrees,
raw Vicon X/Y, and lap number. Samples that jump more than `0.10 m` are rejected
by default; change this using `--max-jump`.

## Preserved original material

`legacy/` is an unchanged copy of the original SPARCS folder, including:

- `vicon.py`
- `sparcs_pi.py` lap and camera logger
- `sparcs_data_generation.py`
- `create_path.py`
- precise, internal and external `.npy` lap paths
- SPARCS test-map images
- network configuration

Those scripts use the old ROS 1 `stuff` compatibility layer and are retained as
reference data. Use `vicon_xy_logger.py` for ROS 2 Jazzy measurements.
