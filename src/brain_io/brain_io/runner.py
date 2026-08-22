#!/usr/bin/env python3
# Purpose: Construct the selected adapter and run the Brain state machine.
# Inputs: CLI mode/checkpoint arguments, ROS topics, map asset, and optional camera frames.
# Outputs: Running Brain node, vehicle commands, visualisation, and process exit status.

"""Composition root for the UniPD DriveOps brain.
This is the only module that selects a physical or simulated vehicle adapter.
Core perception, planning, state-machine and controller modules remain unaware
of that choice.
"""

import argparse
import csv
import os
import threading
from datetime import datetime
from time import sleep, time

import cv2 as cv
import rclpy
from rclpy.executors import ExternalShutdownException

from brain_core.common import constants as nac
from brain_core.common import geometry as geometry
from brain_core.common.resources import data_path, state_path
from brain_core.controllers.speed import ControllerSpeed
from brain_core.controllers.steering import Controller
from brain_core.controllers.path_following import CheckpointFollower
from brain_core.perception.detection import Detection
from brain_core.planning.path_planner import PathPlanning


TARGET_FPS = 30.0
DESIRED_SPEED = 0.25


def _parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Run the UniPD DriveOps brain')
    parser.add_argument('--mode', choices=('hardware', 'simulation'), default='hardware')
    parser.add_argument('--sim', action='store_true', help='Alias for --mode simulation')
    parser.add_argument('--random', action='store_true')
    parser.add_argument('--rc', action='store_true')
    parser.add_argument('--show', action='store_true')
    parser.add_argument('--arena', action='store_true')
    parser.add_argument('--resume', action='store_true')
    parser.add_argument(
        '--path-only',
        action='store_true',
        help=(
            'simulation test mode: follow graph checkpoints while ignoring '
            'events, stop lines, obstacles and specialised manoeuvres'
        ),
    )
    args, ros_args = parser.parse_known_args(argv)
    if args.sim:
        args.mode = 'simulation'
    if args.path_only and args.mode != 'simulation':
        parser.error('--path-only is restricted to simulation test runs')
    return args, ros_args


def _configure_runtime(args):
    nac.RANDOM_START = args.random
    nac.RC_MODE = args.rc
    nac.SIMULATOR_FLAG = args.mode == 'simulation'
    nac.SHOW_IMGS = args.show
    nac.ARENA = args.arena
    nac.RESUME = args.resume


def _make_car(mode, *, path_only=False):
    options = dict(
        # Checkpoint-only validation has no camera/NN dependency.  Gazebo can
        # still display the OAK stream, but Brain does not subscribe to it.
        trig_cam=not path_only,
        trig_gps=True,
        trig_bno=True,
        trig_enc=True,
        trig_control=True,
        trig_sonar=True,
        trig_lidar=True,
        trig_tof=True,
    )
    if mode == 'simulation':
        from brain_io.adapters.simulator import AutomobileDataSimulator
        return AutomobileDataSimulator(**options)
    from brain_io.adapters.hardware import AutomobileDataPi
    return AutomobileDataPi(**options)


def _spin_car(car):
    """Spin until shutdown without leaking the executor exception on SIGINT."""
    try:
        rclpy.spin(car)
    except ExternalShutdownException:
        pass


def main(argv=None):
    args, ros_args = _parse_args(argv)
    _configure_runtime(args)

    if args.path_only:
        print(
            'PATH-ONLY TEST MODE: stop lines, crosswalks, obstacles and other '
            'event behaviours are disabled.'
        )

    # These modules read runtime flags while defining the competition state
    # machine, so import them only after configuration has been applied.
    from brain_core.state_machine.autonomous import Brain
    from brain_core.state_machine.environment import EnvironmentalData

    rclpy.init(args=ros_args)
    car = _make_car(args.mode, path_only=args.path_only)
    spin_thread = threading.Thread(target=_spin_car, args=(car,), daemon=True)
    spin_thread.start()

    track = cv.imread(data_path('2024_VerySmall.png'))
    if track is None:
        raise FileNotFoundError(data_path('2024_VerySmall.png'))

    geometry.create_frames(nac.SHOW_IMGS)
    path_planner = PathPlanning(track)
    environment = EnvironmentalData(
        car=car, trig_v2v=True, trig_v2x=True, trig_semaphore=True)
    steering = Controller(
        k1=0.0, k2=5.0, k3=1.5, k3_NL=1.3, k3D=0.08,
        dist_point_ahead=0.35, ff=1.0)
    speed = ControllerSpeed(desired_speed=0.35, curve_speed=0.25)
    path_follower = CheckpointFollower(completion_radius_m=0.30)
    # In checkpoint-only mode no perception routine is reachable, so avoid
    # loading the lane/intersection ONNX models altogether.
    detection = None if args.path_only else Detection()

    if nac.RC_MODE:
        from brain_core.state_machine.remote import RC_Brain
        brain = RC_Brain(
            car=car, controller=steering, detection=detection,
            max_speed=DESIRED_SPEED)
    else:
        brain = Brain(
            car=car,
            controller=steering,
            controller_sp=speed,
            detection=detection,
            env=environment,
            path_planner=path_planner,
            path_follower=path_follower,
            path_only=args.path_only,
            desired_speed=DESIRED_SPEED,
        )

    geometry.show_track(track, car, nac.SHOW_IMGS)
    log_path = state_path(
        'logs', f'yaw_distance_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    try:
        car.stop()
        sleep(1.0)
        with open(log_path, 'w', newline='') as log_file:
            writer = csv.writer(log_file)
            writer.writerow(['timestamp', 'encoder_distance', 'yaw_true'])
            while rclpy.ok():
                started = time()
                writer.writerow([started, car.encoder_distance, car.yaw_true])

                if car.frame is None and not args.path_only:
                    sleep(0.05)
                    continue

                brain.run()
                if nac.SHOW_IMGS and cv.waitKey(1) == 27:
                    break

                remaining = 1.0 / TARGET_FPS - (time() - started)
                if remaining > 0:
                    sleep(remaining)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            car.stop()
        cv.destroyAllWindows()
        car.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
        spin_thread.join(timeout=2.0)


if __name__ == '__main__':
    main()
