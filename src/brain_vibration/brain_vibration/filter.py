"""Small ROS-independent filters used by the vibration monitor."""

import math


class ExponentialVibrationEstimator:
    """Track the high-frequency RMS residual of a three-axis signal."""

    def __init__(self, time_constant_s: float) -> None:
        self.time_constant_s = max(float(time_constant_s), 1.0e-3)
        self.mean = [0.0, 0.0, 0.0]
        self.variance = [0.0, 0.0, 0.0]
        self.sample_count = 0

    def update(self, values, dt_s: float) -> None:
        values = [float(value) for value in values]
        if len(values) != 3 or not all(math.isfinite(value) for value in values):
            return

        if self.sample_count == 0:
            self.mean = values
            self.sample_count = 1
            return

        dt_s = min(max(float(dt_s), 1.0e-4), 1.0)
        alpha = 1.0 - math.exp(-dt_s / self.time_constant_s)
        for axis, value in enumerate(values):
            delta = value - self.mean[axis]
            self.mean[axis] += alpha * delta
            # Exponentially weighted variance around the moving baseline.
            self.variance[axis] = (1.0 - alpha) * (
                self.variance[axis] + alpha * delta * delta
            )
        self.sample_count += 1

    @property
    def rms(self):
        return tuple(math.sqrt(max(variance, 0.0)) for variance in self.variance)
