#!/usr/bin/env python3
"""Generate a PNG containing the route used by the Brain checkpoints.

The checkpoint list is imported from ``brain_core.state_machine.autonomous``
after applying the same mode flags used by ``brain_io.runner``.  No ROS node,
simulator, camera, or vehicle is started.
"""

import argparse
from pathlib import Path

import cv2 as cv

from brain_core.common import constants as nac


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("checkpoint_path.png"),
        help="output PNG path (default: checkpoint_path.png)",
    )
    parser.add_argument(
        "--mode", choices=("hardware", "simulation"), default="simulation",
        help="same mode as the Brain run (default: simulation)",
    )
    parser.add_argument("--arena", action="store_true")
    parser.add_argument("--random", action="store_true")
    parser.add_argument(
        "--resume", action="store_true",
        help="read the remaining checkpoints saved by a resumed Brain run",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # These flags must be set before importing autonomous.py because that
    # module selects CHECKPOINTS at import time, just like runner.py does.
    nac.SIMULATOR_FLAG = args.mode == "simulation"
    nac.ARENA = args.arena
    nac.RANDOM_START = args.random
    nac.RESUME = args.resume
    nac.SHOW_IMGS = False

    from brain_core.state_machine.autonomous import CHECKPOINTS
    from brain_core.common.resources import data_path
    from brain_core.planning.path_planner import PathPlanning

    checkpoints = [int(checkpoint) for checkpoint in CHECKPOINTS]
    if len(checkpoints) < 2:
        raise SystemExit("at least two checkpoints are required")

    map_image = cv.imread(data_path("2024_VerySmall.png"))
    if map_image is None:
        raise FileNotFoundError(data_path("2024_VerySmall.png"))

    planner = PathPlanning(map_image)
    for start, end in zip(checkpoints, checkpoints[1:]):
        planner.compute_shortest_path(start, end)
        planner.draw_path()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if not cv.imwrite(str(args.output), planner.map):
        raise SystemExit(f"could not write {args.output}")

    print(f"Checkpoints: {checkpoints}")
    print(f"Saved route PNG: {args.output.resolve()}")


if __name__ == "__main__":
    main()
