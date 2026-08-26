import math

from brain_vibration.filter import ExponentialVibrationEstimator


def test_constant_bias_is_removed():
    estimator = ExponentialVibrationEstimator(0.5)
    for _ in range(500):
        estimator.update((0.0, 0.0, 9.81), 0.01)
    assert estimator.rms[2] < 1.0e-6


def test_oscillation_produces_rms():
    estimator = ExponentialVibrationEstimator(0.5)
    frequency_hz = 5.0
    for index in range(1000):
        value = math.sin(2.0 * math.pi * frequency_hz * index * 0.01)
        estimator.update((0.0, 0.0, value), 0.01)
    assert 0.65 < estimator.rms[2] < 0.75
