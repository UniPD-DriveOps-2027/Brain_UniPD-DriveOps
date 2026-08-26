import math

import pytest

from brain_camera.geometry import cropped_intrinsics, quaternion_to_roll_pitch


def test_quaternion_roll_pitch():
    angle = math.radians(10.0)
    roll, pitch = quaternion_to_roll_pitch(0.0, math.sin(angle / 2), 0.0, math.cos(angle / 2))
    assert roll == pytest.approx(0.0, abs=1.0e-9)
    assert pitch == pytest.approx(angle, abs=1.0e-9)


def test_crop_updates_focal_length_and_principal_point():
    k = [600.0, 0.0, 640.0, 0.0, 600.0, 360.0, 0.0, 0.0, 1.0]
    p = [600.0, 0.0, 640.0, 0.0, 0.0, 600.0, 360.0, 0.0, 0.0, 0.0, 1.0, 0.0]
    k_out, _, crop_x, crop_y = cropped_intrinsics(k, p, 1280, 720, 0.05, 0.08)
    assert (crop_x, crop_y) == (64, 58)
    assert k_out[0] > k[0]
    assert k_out[4] > k[4]
    assert k_out[2] == pytest.approx(640.0)
    assert k_out[5] == pytest.approx(360.0, abs=1.0)
