"""ROS-independent camera-stabilization geometry helpers."""

import math


def wrap_angle(angle: float) -> float:
    return math.atan2(math.sin(angle), math.cos(angle))


def quaternion_to_roll_pitch(x: float, y: float, z: float, w: float):
    norm = math.sqrt(x * x + y * y + z * z + w * w)
    if norm < 1.0e-9:
        raise ValueError('invalid zero-length quaternion')
    x, y, z, w = x / norm, y / norm, z / norm, w / norm
    roll = math.atan2(
        2.0 * (w * x + y * z),
        1.0 - 2.0 * (x * x + y * y),
    )
    sin_pitch = max(-1.0, min(1.0, 2.0 * (w * y - z * x)))
    pitch = math.asin(sin_pitch)
    return roll, pitch


def cropped_intrinsics(k, p, width, height, crop_x_fraction, crop_y_fraction):
    crop_x = int(round(width * max(0.0, min(crop_x_fraction, 0.45))))
    crop_y = int(round(height * max(0.0, min(crop_y_fraction, 0.45))))
    inner_width = max(width - 2 * crop_x, 1)
    inner_height = max(height - 2 * crop_y, 1)
    scale_x = width / inner_width
    scale_y = height / inner_height

    k_out = list(k)
    p_out = list(p)
    k_out[0] *= scale_x
    k_out[2] = (k_out[2] - crop_x) * scale_x
    k_out[4] *= scale_y
    k_out[5] = (k_out[5] - crop_y) * scale_y
    p_out[0] *= scale_x
    p_out[2] = (p_out[2] - crop_x) * scale_x
    p_out[5] *= scale_y
    p_out[6] = (p_out[6] - crop_y) * scale_y
    p_out[3] *= scale_x
    p_out[7] *= scale_y
    return k_out, p_out, crop_x, crop_y
