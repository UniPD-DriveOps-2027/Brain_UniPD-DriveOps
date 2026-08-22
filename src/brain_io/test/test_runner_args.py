# Purpose: Verify Brain runner command-line argument handling.
# Inputs: Representative CLI argument lists.
# Outputs: Pytest assertions for selected adapter and path-only options.


import pytest

from brain_io.runner import _parse_args


def test_path_only_is_available_for_simulation():
    args, ros_args = _parse_args(['--sim', '--path-only'])

    assert args.mode == 'simulation'
    assert args.path_only
    assert ros_args == []


def test_path_only_is_rejected_for_hardware():
    with pytest.raises(SystemExit):
        _parse_args(['--mode', 'hardware', '--path-only'])