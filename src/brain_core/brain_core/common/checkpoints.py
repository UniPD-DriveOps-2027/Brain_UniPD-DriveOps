"""Load fixed checkpoint routes shared by the Brain and tools."""

import json

from brain_core.common.resources import data_path


def checkpoint_routes():
    with open(data_path("checkpoints.json"), encoding="utf-8") as file:
        routes = json.load(file)
    return {name: [int(node) for node in nodes] for name, nodes in routes.items()}
