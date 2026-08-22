# Purpose: Follow graph checkpoint paths with a geometric Pure Pursuit controller.
# Inputs: Nx2 graph-frame path, vehicle x/y/yaw, speed, and update time.
# Outputs: Steering command plus progress, target, validity, and completion telemetry.


"""Checkpoint-path following without camera or neural-network input.

The controller follows an ordered polyline using pure pursuit.  Positions are
metres in the Brain map frame, yaw is radians, and the returned steering angle
is degrees, matching the vehicle command interface.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Optional, Sequence, Tuple

import numpy as np


_EPSILON = 1.0e-9


def _wrap_angle(angle: float) -> float:
    """Wrap an angle to [-pi, pi]."""

    return math.atan2(math.sin(angle), math.cos(angle))


def pure_pursuit_steering_deg(
    target_x: float,
    target_y: float,
    x: float,
    y: float,
    yaw: float,
    *,
    wheelbase_m: float = 0.26,
    max_steering_deg: float = 28.0,
) -> float:
    """Return an Ackermann steering command for one lookahead target.

    Positive degrees turn left and negative degrees turn right.  This matches
    the Gazebo Ackermann plugin's implemented joint convention and keeps the
    controller in the standard x-forward, y-left vehicle frame.
    """

    if wheelbase_m <= 0.0:
        raise ValueError("wheelbase_m must be positive")
    if max_steering_deg <= 0.0:
        raise ValueError("max_steering_deg must be positive")

    values = (target_x, target_y, x, y, yaw)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("target and pose values must be finite")

    dx = target_x - x
    dy = target_y - y
    lookahead_distance = math.hypot(dx, dy)
    if lookahead_distance <= _EPSILON:
        return 0.0

    alpha = _wrap_angle(math.atan2(dy, dx) - yaw)
    steering_rad = math.atan2(
        2.0 * wheelbase_m * math.sin(alpha),
        lookahead_distance,
    )
    steering_deg = math.degrees(steering_rad)
    return float(np.clip(
        steering_deg,
        -max_steering_deg,
        max_steering_deg,
    ))


@dataclass(frozen=True)
class PathFollowingCommand:
    """One checkpoint-follower update and its diagnostic metadata."""

    steering_deg: float
    target: Optional[Tuple[float, float]]
    target_index: Optional[int]
    nearest_index: Optional[int]
    cross_track_error_m: float
    heading_error_rad: float
    lookahead_m: float
    progress_m: float
    remaining_m: float
    distance_to_goal_m: float
    route_complete: bool
    reacquired: bool
    has_path: bool


class CheckpointFollower:
    """Stateful pure-pursuit controller for an ordered ``N x 2`` path.

    Progress is monotonic during a route.  The normal nearest-point search is
    limited to a local forward section, preventing jumps at crossings.  When
    that section is farther than ``reacquire_distance_m``, the controller
    searches the entire remaining route and resumes at the closest point.

    Call :meth:`set_path` whenever the planned route changes.  This removes
    consecutive duplicate points and resets all progress state.
    """

    def __init__(
        self,
        path: Optional[Sequence[Sequence[float]]] = None,
        *,
        wheelbase_m: float = 0.26,
        min_lookahead_m: float = 0.35,
        lookahead_speed_gain_s: float = 0.60,
        max_lookahead_m: float = 0.80,
        max_steering_deg: float = 28.0,
        reacquire_distance_m: float = 0.75,
        local_search_distance_m: float = 2.0,
        completion_radius_m: float = 0.15,
        duplicate_tolerance_m: float = 1.0e-6,
    ) -> None:
        if wheelbase_m <= 0.0:
            raise ValueError("wheelbase_m must be positive")
        if min_lookahead_m <= 0.0:
            raise ValueError("min_lookahead_m must be positive")
        if lookahead_speed_gain_s < 0.0:
            raise ValueError("lookahead_speed_gain_s cannot be negative")
        if max_lookahead_m < min_lookahead_m:
            raise ValueError(
                "max_lookahead_m must be at least min_lookahead_m"
            )
        if max_steering_deg <= 0.0:
            raise ValueError("max_steering_deg must be positive")
        if reacquire_distance_m <= 0.0:
            raise ValueError("reacquire_distance_m must be positive")
        if local_search_distance_m <= 0.0:
            raise ValueError("local_search_distance_m must be positive")
        if completion_radius_m < 0.0:
            raise ValueError("completion_radius_m cannot be negative")
        if duplicate_tolerance_m < 0.0:
            raise ValueError("duplicate_tolerance_m cannot be negative")

        self.wheelbase_m = float(wheelbase_m)
        self.min_lookahead_m = float(min_lookahead_m)
        self.lookahead_speed_gain_s = float(lookahead_speed_gain_s)
        self.max_lookahead_m = float(max_lookahead_m)
        self.max_steering_deg = float(max_steering_deg)
        self.reacquire_distance_m = float(reacquire_distance_m)
        self.local_search_distance_m = float(local_search_distance_m)
        self.completion_radius_m = float(completion_radius_m)
        self.duplicate_tolerance_m = float(duplicate_tolerance_m)

        self._path = np.empty((0, 2), dtype=float)
        self._original_indices = np.empty((0,), dtype=int)
        self._segment_vectors = np.empty((0, 2), dtype=float)
        self._segment_lengths = np.empty((0,), dtype=float)
        self._cumulative_lengths = np.empty((0,), dtype=float)
        self._progress_m = 0.0
        self._has_pose = False
        self.set_path([] if path is None else path)

    @property
    def path(self) -> np.ndarray:
        """Return a copy of the de-duplicated route."""

        return self._path.copy()

    @property
    def progress_m(self) -> float:
        """Distance already travelled along the current route."""

        return self._progress_m

    @property
    def route_length_m(self) -> float:
        """Total length of the current route."""

        if self._cumulative_lengths.size == 0:
            return 0.0
        return float(self._cumulative_lengths[-1])

    def set_path(self, path: Sequence[Sequence[float]]) -> None:
        """Install a new route and reset its progress.

        Indices in command metadata refer to the corresponding points in the
        caller's original path, including when duplicates have been removed.
        """

        points = np.asarray(path, dtype=float)
        if points.size == 0:
            points = np.empty((0, 2), dtype=float)
        if points.ndim != 2 or points.shape[1] != 2:
            raise ValueError("path must have shape (N, 2)")
        if not np.all(np.isfinite(points)):
            raise ValueError("path coordinates must be finite")

        if len(points) > 1:
            step_lengths = np.linalg.norm(np.diff(points, axis=0), axis=1)
            keep = np.concatenate((
                np.array([True]),
                step_lengths > self.duplicate_tolerance_m,
            ))
        else:
            keep = np.ones((len(points),), dtype=bool)

        self._path = points[keep].copy()
        self._original_indices = np.flatnonzero(keep)
        self._segment_vectors = np.diff(self._path, axis=0)
        if len(self._segment_vectors) > 0:
            self._segment_lengths = np.linalg.norm(
                self._segment_vectors,
                axis=1,
            )
            self._cumulative_lengths = np.concatenate((
                np.array([0.0]),
                np.cumsum(self._segment_lengths),
            ))
        elif len(self._path) == 1:
            self._segment_lengths = np.empty((0,), dtype=float)
            self._cumulative_lengths = np.array([0.0])
        else:
            self._segment_lengths = np.empty((0,), dtype=float)
            self._cumulative_lengths = np.empty((0,), dtype=float)

        self.reset()

    def reset(self) -> None:
        """Reset progress while keeping the current route."""

        self._progress_m = 0.0
        self._has_pose = False

    def lookahead_for_speed(self, speed_mps: float) -> float:
        """Return the configured speed-dependent lookahead distance."""

        if not math.isfinite(speed_mps):
            raise ValueError("speed_mps must be finite")
        lookahead = (
            self.min_lookahead_m
            + self.lookahead_speed_gain_s * abs(speed_mps)
        )
        return float(min(lookahead, self.max_lookahead_m))

    def update(
        self,
        x: float,
        y: float,
        yaw: float,
        speed_mps: float,
    ) -> PathFollowingCommand:
        """Update route progress and return a steering command."""

        if not all(math.isfinite(value) for value in (x, y, yaw, speed_mps)):
            raise ValueError("pose and speed values must be finite")

        lookahead_m = self.lookahead_for_speed(speed_mps)
        if len(self._path) == 0:
            return PathFollowingCommand(
                steering_deg=0.0,
                target=None,
                target_index=None,
                nearest_index=None,
                cross_track_error_m=0.0,
                heading_error_rad=0.0,
                lookahead_m=lookahead_m,
                progress_m=0.0,
                remaining_m=0.0,
                distance_to_goal_m=0.0,
                route_complete=False,
                reacquired=False,
                has_path=False,
            )

        position = np.array([x, y], dtype=float)
        if len(self._path) == 1:
            return self._update_single_point(
                position,
                yaw,
                lookahead_m,
            )

        (
            _,
            segment_index,
            projected_s,
            reacquired,
        ) = self._nearest_forward_projection(position)
        self._progress_m = max(self._progress_m, projected_s)
        projection, progress_segment, _ = self._point_at_s(self._progress_m)

        target_s = min(
            self._progress_m + lookahead_m,
            self.route_length_m,
        )
        target, _, target_point_index = self._point_at_s(target_s)
        nearest_point_index = self._nearest_endpoint_index(
            position,
            segment_index,
        )

        # Do not normalize the stored segment in place: NumPy indexing returns
        # a view, so in-place division would shrink the route geometry again on
        # every controller update.
        tangent = (
            self._segment_vectors[progress_segment]
            / self._segment_lengths[progress_segment]
        )
        position_error = position - projection
        cross_track_error_m = float(
            tangent[0] * position_error[1]
            - tangent[1] * position_error[0]
        )
        route_heading = math.atan2(tangent[1], tangent[0])
        heading_error_rad = _wrap_angle(route_heading - yaw)

        distance_to_goal_m = float(np.linalg.norm(
            self._path[-1] - position,
        ))
        remaining_m = max(0.0, self.route_length_m - self._progress_m)
        # A route may loop back close to its endpoint. Euclidean distance alone
        # would then complete it before the ordered path has been followed.
        route_complete = (
            remaining_m <= self.completion_radius_m
            and distance_to_goal_m <= self.completion_radius_m
        )
        steering_deg = 0.0 if route_complete else pure_pursuit_steering_deg(
            float(target[0]),
            float(target[1]),
            x,
            y,
            yaw,
            wheelbase_m=self.wheelbase_m,
            max_steering_deg=self.max_steering_deg,
        )

        self._has_pose = True
        return PathFollowingCommand(
            steering_deg=steering_deg,
            target=(float(target[0]), float(target[1])),
            target_index=int(self._original_indices[target_point_index]),
            nearest_index=int(self._original_indices[nearest_point_index]),
            cross_track_error_m=cross_track_error_m,
            heading_error_rad=heading_error_rad,
            lookahead_m=lookahead_m,
            progress_m=self._progress_m,
            remaining_m=remaining_m,
            distance_to_goal_m=distance_to_goal_m,
            route_complete=route_complete,
            reacquired=reacquired,
            has_path=True,
        )

    # ``compute`` is convenient for integrations that name controller calls by
    # output rather than state update.
    compute = update

    def _update_single_point(
        self,
        position: np.ndarray,
        yaw: float,
        lookahead_m: float,
    ) -> PathFollowingCommand:
        target = self._path[0]
        delta = target - position
        distance_to_goal_m = float(np.linalg.norm(delta))
        bearing_error = _wrap_angle(
            math.atan2(delta[1], delta[0]) - yaw
        ) if distance_to_goal_m > _EPSILON else 0.0
        cross_track_error_m = distance_to_goal_m * math.sin(bearing_error)
        # A one-point route has no along-path distance, so proximity is the
        # only meaningful completion criterion.
        route_complete = distance_to_goal_m <= self.completion_radius_m
        steering_deg = 0.0 if route_complete else pure_pursuit_steering_deg(
            float(target[0]),
            float(target[1]),
            float(position[0]),
            float(position[1]),
            yaw,
            wheelbase_m=self.wheelbase_m,
            max_steering_deg=self.max_steering_deg,
        )
        self._has_pose = True
        return PathFollowingCommand(
            steering_deg=steering_deg,
            target=(float(target[0]), float(target[1])),
            target_index=int(self._original_indices[0]),
            nearest_index=int(self._original_indices[0]),
            cross_track_error_m=cross_track_error_m,
            heading_error_rad=bearing_error,
            lookahead_m=lookahead_m,
            progress_m=0.0,
            remaining_m=0.0,
            distance_to_goal_m=distance_to_goal_m,
            route_complete=route_complete,
            reacquired=False,
            has_path=True,
        )

    def _nearest_forward_projection(
        self,
        position: np.ndarray,
    ) -> Tuple[np.ndarray, int, float, bool]:
        segment_count = len(self._segment_lengths)
        if not self._has_pose:
            projection, segment_index, projected_s, _ = \
                self._project_onto_segments(
                    position,
                    np.arange(segment_count),
                )
            return projection, segment_index, projected_s, False

        start_segment = self._segment_index_at_s(self._progress_m)
        local_end_s = min(
            self.route_length_m,
            self._progress_m + self.local_search_distance_m,
        )
        end_segment = self._segment_index_at_s(local_end_s)
        local_indices = np.arange(start_segment, end_segment + 1)
        local_result = self._project_onto_segments(position, local_indices)
        if local_result[3] <= self.reacquire_distance_m:
            projection, segment_index, projected_s, _ = local_result
            return (
                projection,
                segment_index,
                max(projected_s, self._progress_m),
                False,
            )

        forward_indices = np.arange(start_segment, segment_count)
        projection, segment_index, projected_s, _ = \
            self._project_onto_segments(position, forward_indices)
        return (
            projection,
            segment_index,
            max(projected_s, self._progress_m),
            True,
        )

    def _project_onto_segments(
        self,
        position: np.ndarray,
        segment_indices: np.ndarray,
    ) -> Tuple[np.ndarray, int, float, float]:
        starts = self._path[segment_indices]
        vectors = self._segment_vectors[segment_indices]
        lengths = self._segment_lengths[segment_indices]
        offsets = position - starts
        fractions = np.einsum("ij,ij->i", offsets, vectors) / (lengths ** 2)
        fractions = np.clip(fractions, 0.0, 1.0)
        projections = starts + fractions[:, np.newaxis] * vectors
        distances = np.linalg.norm(projections - position, axis=1)
        best_local_index = int(np.argmin(distances))
        segment_index = int(segment_indices[best_local_index])
        projected_s = float(
            self._cumulative_lengths[segment_index]
            + fractions[best_local_index] * self._segment_lengths[segment_index]
        )
        return (
            projections[best_local_index],
            segment_index,
            projected_s,
            float(distances[best_local_index]),
        )

    def _segment_index_at_s(self, distance_m: float) -> int:
        index = int(np.searchsorted(
            self._cumulative_lengths,
            distance_m,
            side="right",
        )) - 1
        return min(max(index, 0), len(self._segment_lengths) - 1)

    def _point_at_s(
        self,
        distance_m: float,
    ) -> Tuple[np.ndarray, int, int]:
        distance_m = float(np.clip(distance_m, 0.0, self.route_length_m))
        segment_index = self._segment_index_at_s(distance_m)
        segment_start_s = self._cumulative_lengths[segment_index]
        fraction = (
            (distance_m - segment_start_s)
            / self._segment_lengths[segment_index]
        )
        point = (
            self._path[segment_index]
            + fraction * self._segment_vectors[segment_index]
        )
        point_index = int(np.searchsorted(
            self._cumulative_lengths,
            distance_m,
            side="left",
        ))
        return point, segment_index, point_index

    def _nearest_endpoint_index(
        self,
        position: np.ndarray,
        segment_index: int,
    ) -> int:
        first_distance = np.linalg.norm(
            position - self._path[segment_index]
        )
        second_distance = np.linalg.norm(
            position - self._path[segment_index + 1]
        )
        if second_distance < first_distance:
            return segment_index + 1
        return segment_index