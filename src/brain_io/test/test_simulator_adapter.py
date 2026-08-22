# Purpose: Verify simulator coordinate, heading, command, and odometry adaptation.
# Inputs: Synthetic Gazebo messages, poses, yaw values, and odometry samples.
# Outputs: Pytest assertions for normalised state and command contracts.


import math

import pytest

from brain_io.adapters.simulator import (
    BRAIN_MAP_WIDTH_M,
    GAZEBO_TO_BRAIN_X_SCALE,
    GAZEBO_TO_BRAIN_Y_SCALE,
    _accumulate_odometry_distance,
    _core_speed_to_simulator,
    _normalize_angle,
    _simulator_position_to_brain,
    _simulator_world_position_to_brain,
    _simulator_yaw_to_brain,
)


def test_simulator_track_corners_map_to_brain_map_extent():
    assert _simulator_position_to_brain(0.0, 0.0) == (0.0, 15.0)
    x, y = _simulator_position_to_brain(14.68, 14.99)
    assert x == pytest.approx(BRAIN_MAP_WIDTH_M)
    assert y == pytest.approx(0.0)


def test_normal_spawn_maps_to_graph_start_node():
    # GPS antenna mean at the normal Gazebo spawn (model x minus 0.077 m).
    x, y = _simulator_position_to_brain(8.373, 12.97)
    assert x == pytest.approx(12.8973040221)
    assert y == pytest.approx(2.0213475650)


def test_normal_world_odometry_maps_to_current_graph_pose():
    x, y = _simulator_world_position_to_brain(8.45, -12.97)
    assert x == pytest.approx(13.0159105442)
    assert y == pytest.approx(2.0213475650)


@pytest.mark.parametrize(
    ('simulator_yaw', 'brain_yaw'),
    [
        (0.0, 0.0),
        (math.pi / 2.0, math.pi / 2.0),
        (-math.pi / 2.0, -math.pi / 2.0),
    ],
)
def test_cardinal_yaw_is_mapped_into_brain_frame(
        simulator_yaw, brain_yaw):
    assert _simulator_yaw_to_brain(simulator_yaw) == pytest.approx(brain_yaw)


def test_diagonal_yaw_accounts_for_anisotropic_track_scale():
    expected = math.atan2(
        GAZEBO_TO_BRAIN_Y_SCALE,
        GAZEBO_TO_BRAIN_X_SCALE,
    )
    assert _simulator_yaw_to_brain(math.pi / 4.0) == pytest.approx(expected)


@pytest.mark.parametrize(
    ('core_speed', 'wire_speed'),
    [(0.0, 0.0), (0.3, 0.1), (-0.3, -0.1)],
)
def test_speed_command_compensates_gazebo_plugin(core_speed, wire_speed):
    assert _core_speed_to_simulator(core_speed) == pytest.approx(wire_speed)


def test_angle_normalization_preserves_radian_contract():
    assert _normalize_angle(3.0 * math.pi) == pytest.approx(math.pi)
    assert _normalize_angle(-3.0 * math.pi) == pytest.approx(-math.pi)


def test_odometry_distance_is_cumulative_and_unsigned():
    total, previous, rejected = _accumulate_odometry_distance(
        0.0, None, (8.45, -12.97))
    assert total == 0.0
    assert not rejected

    total, previous, rejected = _accumulate_odometry_distance(
        total, previous, (8.55, -12.97))
    assert total == pytest.approx(0.1)
    assert not rejected

    total, previous, rejected = _accumulate_odometry_distance(
        total, previous, (8.50, -12.97))
    assert total == pytest.approx(0.15)
    assert not rejected


def test_odometry_distance_ignores_model_respawn_jump():
    total, previous, rejected = _accumulate_odometry_distance(
        4.2, (18.0, -1.0), (8.45, -12.97))
    assert total == pytest.approx(4.2)
    assert previous == (8.45, -12.97)
    assert rejected

    total, _, rejected = _accumulate_odometry_distance(
        total, previous, (8.46, -12.97))
    assert total == pytest.approx(4.21)
    assert not rejected