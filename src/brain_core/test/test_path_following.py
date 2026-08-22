# Purpose: Verify Pure Pursuit path-following geometry and safety behaviour.
# Inputs: Synthetic paths, poses, speeds, and controller configurations.
# Outputs: Pytest assertions for steering, progress, reacquisition, and completion.


import math

import numpy as np
import pytest

from brain_core.controllers.path_following import (
    CheckpointFollower,
    pure_pursuit_steering_deg,
)


def test_straight_path_produces_zero_steering_and_low_speed_lookahead():
    follower = CheckpointFollower([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0]])

    command = follower.update(0.1, 0.0, 0.0, 0.25)

    assert command.steering_deg == pytest.approx(0.0)
    assert command.lookahead_m == pytest.approx(0.50)
    assert command.target == pytest.approx((0.60, 0.0))
    assert command.target_index == 1
    assert command.cross_track_error_m == pytest.approx(0.0)
    assert command.has_path


def test_pure_pursuit_sign_and_steering_limit():
    left = pure_pursuit_steering_deg(0.005, 0.1, 0.0, 0.0, 0.0)
    right = pure_pursuit_steering_deg(0.005, -0.1, 0.0, 0.0, 0.0)

    # Gazebo's Ackermann implementation uses positive-left/negative-right.
    assert left == pytest.approx(28.0)
    assert right == pytest.approx(-28.0)


def test_progress_does_not_move_backwards_with_pose_jitter():
    path = np.column_stack((np.arange(0.0, 4.1, 0.1), np.zeros(41)))
    follower = CheckpointFollower(path)

    first = follower.update(1.20, 0.02, 0.0, 0.25)
    second = follower.update(1.15, -0.01, 0.0, 0.25)

    assert first.progress_m == pytest.approx(1.20)
    assert second.progress_m == pytest.approx(first.progress_m)
    assert second.target_index >= first.target_index
    assert not second.reacquired


def test_repeated_updates_do_not_mutate_path_geometry():
    path = np.column_stack((np.arange(0.0, 2.1, 0.1), np.zeros(21)))
    follower = CheckpointFollower(path)

    for _ in range(100):
        command = follower.update(0.5, 0.1, 0.0, 0.25)

    assert follower.path == pytest.approx(path)
    assert command.cross_track_error_m == pytest.approx(0.1)
    assert command.progress_m == pytest.approx(0.5)


def test_controller_reacquires_a_far_forward_route_section():
    path = np.column_stack((np.arange(0.0, 10.1, 0.1), np.zeros(101)))
    follower = CheckpointFollower(path, local_search_distance_m=1.0)
    follower.update(0.10, 0.0, 0.0, 0.25)

    command = follower.update(7.0, 0.10, 0.0, 0.25)

    assert command.reacquired
    assert command.progress_m == pytest.approx(7.0)
    assert command.nearest_index == 70
    assert command.target_index == 75


def test_far_backward_pose_cannot_reverse_route_progress():
    path = np.column_stack((np.arange(0.0, 10.1, 0.1), np.zeros(101)))
    follower = CheckpointFollower(path, local_search_distance_m=1.0)
    follower.update(6.0, 0.0, 0.0, 0.25)

    command = follower.update(1.0, 0.0, 0.0, 0.25)

    assert command.reacquired
    assert command.progress_m == pytest.approx(6.0)
    assert command.target_index == 65


def test_empty_path_returns_safe_neutral_command():
    follower = CheckpointFollower([])

    command = follower.update(1.0, 2.0, 0.5, 0.25)

    assert command.steering_deg == 0.0
    assert command.target is None
    assert command.target_index is None
    assert command.nearest_index is None
    assert not command.has_path
    assert not command.route_complete


def test_single_point_path_steers_and_completes_inside_radius():
    follower = CheckpointFollower([[1.0, 1.0]])

    approaching = follower.update(0.0, 0.0, 0.0, 0.25)
    arrived = follower.update(0.95, 1.0, 0.0, 0.25)

    assert approaching.steering_deg > 0.0
    assert approaching.target_index == 0
    assert not approaching.route_complete
    assert arrived.route_complete
    assert arrived.steering_deg == 0.0


def test_route_does_not_complete_near_goal_until_progress_is_near_end():
    # The endpoint is spatially identical to the start, as on a closed loop.
    follower = CheckpointFollower(
        [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]],
        completion_radius_m=0.30,
        local_search_distance_m=1.0,
    )

    at_start = follower.update(0.0, 0.0, 0.0, 0.25)

    assert at_start.distance_to_goal_m == pytest.approx(0.0)
    assert at_start.remaining_m == pytest.approx(8.0)
    assert not at_start.route_complete


def test_multi_point_route_completes_near_final_progress_and_stops_steering():
    follower = CheckpointFollower(
        [[0.0, 0.0], [1.0, 0.0], [2.0, 0.0]],
        completion_radius_m=0.30,
    )

    command = follower.update(1.85, 0.05, 0.0, 0.25)

    assert command.remaining_m == pytest.approx(0.15)
    assert command.distance_to_goal_m < 0.30
    assert command.route_complete
    assert command.steering_deg == 0.0


def test_duplicate_points_are_removed_but_indices_reference_input_path():
    follower = CheckpointFollower([
        [0.0, 0.0],
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 0.0],
        [2.0, 0.0],
    ])

    command = follower.update(0.0, 0.0, 0.0, 0.25)

    assert follower.path.shape == (3, 2)
    assert command.target_index == 2
    assert math.isfinite(command.steering_deg)


def test_setting_a_new_route_resets_progress():
    old_path = np.column_stack((np.arange(11.0), np.zeros(11)))
    follower = CheckpointFollower(old_path)
    follower.update(8.0, 0.0, 0.0, 0.25)
    assert follower.progress_m == pytest.approx(8.0)

    follower.set_path([[0.0, 0.0], [0.0, 1.0], [0.0, 2.0]])
    assert follower.progress_m == 0.0
    command = follower.update(0.0, 0.10, math.pi / 2.0, 0.25)

    assert command.progress_m == pytest.approx(0.10)
    assert command.target == pytest.approx((0.0, 0.60))
    assert command.steering_deg == pytest.approx(0.0)


def test_route_does_not_complete_early_when_endpoint_is_near_start():
    follower = CheckpointFollower([
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
        [0.0, 0.05],
    ], completion_radius_m=0.15)

    command = follower.update(0.0, 0.0, 0.0, 0.25)

    assert command.distance_to_goal_m < 0.15
    assert command.remaining_m > 3.0
    assert not command.route_complete


def test_cross_track_and_heading_metadata_have_documented_signs():
    follower = CheckpointFollower([[0.0, 0.0], [2.0, 0.0]])

    command = follower.update(0.5, 0.2, math.radians(10.0), 0.25)

    # Vehicle is left of an eastbound path; desired heading is 10 degrees right.
    assert command.cross_track_error_m == pytest.approx(0.2)
    assert command.heading_error_rad == pytest.approx(math.radians(-10.0))


@pytest.mark.parametrize(
    "bad_path",
    [
        [0.0, 1.0],
        [[0.0, 1.0, 2.0]],
        [[0.0, float("nan")]],
    ],
)
def test_invalid_paths_are_rejected(bad_path):
    with pytest.raises(ValueError):
        CheckpointFollower(bad_path)