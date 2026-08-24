# Purpose: Verify classical OpenCV lane-centre detection and route blending.
# Inputs: Synthetic camera frames and steering commands.
# Outputs: Stable lane observations, correct steering signs, and safe fallback.

import cv2 as cv
import numpy as np
import pytest

from brain_core.perception.opencv_lane_center import (
    OpenCVLaneCenter,
    fuse_route_and_lane_steering,
)


def _lane_frame(shift=0):
    frame = np.zeros((240, 320, 3), dtype=np.uint8)
    cv.line(frame, (55 + shift, 239), (145 + shift, 84), (255, 255, 255), 6)
    cv.line(frame, (265 + shift, 239), (175 + shift, 84), (255, 255, 255), 6)
    return frame


def test_opencv_lane_center_detects_a_straight_lane():
    observation = OpenCVLaneCenter().detect(_lane_frame(), visualize=True)

    assert observation.valid
    assert observation.confidence == pytest.approx(1.0)
    assert observation.center_x_px == pytest.approx(160.0, abs=2.0)
    assert observation.steering_deg == pytest.approx(0.0, abs=2.0)
    assert observation.debug_frame.shape == (240, 320, 3)
    assert observation.mask.shape == (240, 320)
    assert observation.mask.dtype == np.uint8
    assert np.count_nonzero(observation.mask) > 0


def test_opencv_lane_center_steering_sign_corrects_lateral_offset():
    lane_left = OpenCVLaneCenter().detect(_lane_frame(shift=-30))
    lane_right = OpenCVLaneCenter().detect(_lane_frame(shift=30))

    assert lane_left.valid and lane_right.valid
    assert lane_left.steering_deg > 0.0
    assert lane_right.steering_deg < 0.0


def test_route_projection_is_used_as_curved_reference():
    route = np.array([
        [160.0, 100.0],
        [158.0, 125.0],
        [154.0, 150.0],
        [149.0, 175.0],
        [143.0, 200.0],
    ], dtype=np.float32)
    observation = OpenCVLaneCenter().detect(
        _lane_frame(),
        route_points_px=route,
        visualize=True,
    )

    assert observation.valid
    assert observation.route_centerline_px is not None
    assert len(observation.route_centerline_px) >= 3
    assert observation.debug_frame.shape == (240, 320, 3)


def test_opencv_lane_center_falls_back_when_no_lane_is_visible():
    observation = OpenCVLaneCenter().detect(
        np.zeros((240, 320, 3), dtype=np.uint8)
    )

    assert not observation.valid
    assert observation.confidence == 0.0
    assert observation.steering_deg == 0.0


def test_route_steering_remains_dominant_in_large_turns():
    straight = fuse_route_and_lane_steering(0.0, 20.0, 1.0)
    turn = fuse_route_and_lane_steering(26.0, -20.0, 1.0)

    assert straight == pytest.approx(11.0)
    assert turn > 15.0
