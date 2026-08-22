# Purpose: Verify checkpoint-only state-machine integration.
# Inputs: Fake vehicle/planner/detection objects and path-only Brain states.
# Outputs: Pytest assertions that routing bypasses camera/event steering safely.


from types import SimpleNamespace
from unittest.mock import Mock, call

from brain_core.common import constants as nac
from brain_core.state_machine.autonomous import (
    Brain,
    checkpoint_route_complete,
)


def _command(*, complete=False, remaining=1.0, goal_distance=1.0):
    return SimpleNamespace(
        has_path=True,
        route_complete=complete,
        remaining_m=remaining,
        distance_to_goal_m=goal_distance,
    )


def test_checkpoint_completion_requires_a_path_and_endpoint_proximity():
    assert not checkpoint_route_complete(None)
    assert not checkpoint_route_complete(SimpleNamespace(has_path=False))
    assert not checkpoint_route_complete(_command())
    assert checkpoint_route_complete(_command(remaining=0.1, goal_distance=0.2))
    assert checkpoint_route_complete(_command(complete=True))


def test_path_only_lane_state_does_not_enter_event_logic_before_endpoint():
    brain = Brain.__new__(Brain)
    brain.path_only = True
    brain.path_following_command = _command()
    brain.activate_routines = Mock()
    brain.next_checkpoint = Mock()
    brain.switch_to_state = Mock()

    Brain.lane_following(brain)

    brain.activate_routines.assert_called_once_with([
        nac.FOLLOW_LANE,
        nac.DRIVE_DESIRED_SPEED,
    ])
    brain.next_checkpoint.assert_not_called()
    brain.switch_to_state.assert_not_called()


def test_path_only_lane_state_advances_once_when_endpoint_is_reached():
    brain = Brain.__new__(Brain)
    brain.path_only = True
    brain.path_following_command = _command(complete=True)
    brain.activate_routines = Mock()
    brain.next_checkpoint = Mock()
    brain.switch_to_state = Mock()

    Brain.lane_following(brain)

    assert brain.activate_routines.call_args_list == [
        call([nac.FOLLOW_LANE, nac.DRIVE_DESIRED_SPEED]),
        call([]),
    ]
    brain.next_checkpoint.assert_called_once_with()
    brain.switch_to_state.assert_called_once_with(nac.START_STATE)


def test_follow_lane_uses_graph_pose_and_forwards_vehicle_steering_sign():
    brain = Brain.__new__(Brain)
    brain.car = SimpleNamespace(
        x_est=12.5,
        y_est=2.0,
        yaw=0.1,
        filtered_encoder_velocity=0.25,
        drive_angle=Mock(),
        stop=Mock(),
    )
    command = SimpleNamespace(has_path=True, steering_deg=-12.0)
    brain.path_follower = SimpleNamespace(update=Mock(return_value=command))
    brain.path_following_command = None

    Brain.follow_lane(brain)

    brain.path_follower.update.assert_called_once_with(
        x=12.5,
        y=2.0,
        yaw=0.1,
        speed_mps=0.25,
    )
    assert brain.path_following_command is command
    brain.car.drive_angle.assert_called_once_with(-12.0)
    brain.car.stop.assert_not_called()