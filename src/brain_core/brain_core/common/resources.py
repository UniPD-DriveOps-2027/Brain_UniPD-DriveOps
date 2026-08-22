# Purpose: Resolve installed Brain asset and writable runtime-state paths.
# Inputs: Relative data/model names and optional state-directory environment configuration.
# Outputs: Absolute filesystem paths for packaged assets and mutable state.


import os
from pathlib import Path


ASSET_ROOT = Path(__file__).resolve().parents[1] / 'assets'
DATA_ROOT = ASSET_ROOT / 'data'
MODEL_ROOT = ASSET_ROOT / 'models'
STATE_ROOT = Path(
    os.environ.get('BRAIN_STATE_DIR', Path.home() / '.local/state/brain_unipd_driveops')
)


def data_path(*parts: str) -> str:
    return str(DATA_ROOT.joinpath(*parts))


def model_path(*parts: str) -> str:
    return str(MODEL_ROOT.joinpath(*parts))


def state_path(*parts: str) -> str:
    STATE_ROOT.mkdir(parents=True, exist_ok=True)
    return str(STATE_ROOT.joinpath(*parts))