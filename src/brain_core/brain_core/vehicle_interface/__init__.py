# Purpose: Define the vehicle_interface Python package namespace.
# Inputs: Imports performed by package consumers.
# Outputs: The importable vehicle_interface package namespace.


"""Vehicle state and hardware/simulator adapters."""

from .automobile_data import Automobile_Data

__all__ = ['Automobile_Data']