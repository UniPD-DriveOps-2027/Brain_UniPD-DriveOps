#!/usr/bin/env python3
# Purpose: Log live Vicon x/y coordinates independently for simulator-map testing.
# Inputs: Vicon host, tracked object name, sampling options, and network frames.
# Outputs: Timestamped coordinate records written to the requested log file.

"""Record actual SPARCS X/Y/yaw coordinates from a ROS 2 Vicon transform."""

import argparse
import csv
import math
from datetime import datetime
from pathlib import Path

import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node


def _yaw(q) -> float:
    return math.atan2(
        2.0 * (q.w * q.z + q.x * q.y),
        1.0 - 2.0 * (q.y * q.y + q.z * q.z),
    )


class ViconXYLogger(Node):
    def __init__(self, options):
        super().__init__('sparcs_vicon_xy_logger')
        self._options = options
        self._previous = None
        self._previous_y = None
        self._lap = 0
        self._last_print_ns = 0

        output = Path(options.output).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        self._file = output.open('w', newline='')
        self._writer = csv.writer(self._file)
        self._writer.writerow([
            'ros_time_s', 'x_m', 'y_m', 'z_m', 'yaw_rad', 'yaw_deg',
            'raw_x_m', 'raw_y_m', 'lap',
        ])

        self.create_subscription(
            TransformStamped, options.topic, self._callback, 20)
        self.get_logger().info(f'Listening on {options.topic}')
        self.get_logger().info(f'Writing actual coordinates to {output}')

    def _callback(self, msg: TransformStamped):
        raw_x = float(msg.transform.translation.x)
        raw_y = float(msg.transform.translation.y)
        z = float(msg.transform.translation.z)
        x = raw_x - self._options.x0
        y = raw_y - self._options.y0
        yaw = math.atan2(
            math.sin(_yaw(msg.transform.rotation) - self._options.yaw_offset),
            math.cos(_yaw(msg.transform.rotation) - self._options.yaw_offset),
        )

        if self._previous is not None:
            jump = math.hypot(x - self._previous[0], y - self._previous[1])
            if jump > self._options.max_jump:
                self.get_logger().warning(
                    f'Rejected {jump:.3f} m Vicon jump at ({x:.3f}, {y:.3f})')
                return

        if self._previous_y is not None:
            crossed = (
                self._previous_y > self._options.lap_y and y <= self._options.lap_y
                if not self._options.reverse
                else self._previous_y < self._options.lap_y and y >= self._options.lap_y
            )
            if crossed:
                self._lap += 1
                self.get_logger().info(f'Completed lap {self._lap}')

        stamp = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        self._writer.writerow([
            f'{stamp:.9f}', f'{x:.6f}', f'{y:.6f}', f'{z:.6f}',
            f'{yaw:.9f}', f'{math.degrees(yaw):.6f}',
            f'{raw_x:.6f}', f'{raw_y:.6f}', self._lap,
        ])
        self._file.flush()
        self._previous = (x, y)
        self._previous_y = y

        now_ns = self.get_clock().now().nanoseconds
        if now_ns - self._last_print_ns >= int(1e9 / self._options.print_hz):
            print(
                f'x={x:8.3f} m  y={y:8.3f} m  '
                f'yaw={math.degrees(yaw):7.2f} deg  lap={self._lap}',
                flush=True,
            )
            self._last_print_ns = now_ns

        if self._options.laps > 0 and self._lap >= self._options.laps:
            self.get_logger().info('Requested lap count reached; stopping.')
            rclpy.shutdown()

    def destroy_node(self):
        self._file.close()
        super().destroy_node()


def _arguments():
    default_name = datetime.now().strftime('vicon_xy_%Y%m%d_%H%M%S.csv')
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', default='/vicon/bfmc_car/bfmc_car')
    parser.add_argument('--output', default=default_name)
    parser.add_argument('--x0', type=float, default=-1.3425)
    parser.add_argument('--y0', type=float, default=-2.35)
    parser.add_argument('--yaw-offset-deg', type=float, default=-90.0)
    parser.add_argument('--max-jump', type=float, default=0.10)
    parser.add_argument('--print-hz', type=float, default=5.0)
    parser.add_argument('--lap-y', type=float, default=2.54)
    parser.add_argument('--laps', type=int, default=0,
                        help='Stop after N laps; zero records indefinitely.')
    parser.add_argument('--reverse', action='store_true')
    options, ros_args = parser.parse_known_args()
    options.yaw_offset = math.radians(options.yaw_offset_deg)
    return options, ros_args


def main():
    options, ros_args = _arguments()
    rclpy.init(args=ros_args)
    node = ViconXYLogger(options)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
