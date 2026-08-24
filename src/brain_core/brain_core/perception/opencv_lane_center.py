# Purpose: Detect visible lane boundaries and estimate the lane centre with OpenCV.
# Inputs: BGR camera frame from the OAK/simulator camera.
# Outputs: Lane-centre offset, heading correction, steering suggestion, and debug image.

"""Lightweight OpenCV lane-centre estimation.

This detector deliberately uses classical image processing only.  The graph
path remains the global route; this module supplies a local correction when
both lane boundaries are visible in the camera image.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Optional, Tuple

import cv2 as cv
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


@dataclass(frozen=True)
class LaneCenterObservation:
    """One camera-frame lane-centre estimate."""

    valid: bool
    center_x_px: Optional[float]
    center_offset_px: float
    heading_error_rad: float
    steering_deg: float
    confidence: float
    left_line: Optional[Tuple[float, float]]
    right_line: Optional[Tuple[float, float]]
    mask: Optional[np.ndarray] = None
    debug_frame: Optional[np.ndarray] = None
    route_centerline_px: Optional[np.ndarray] = None


class OpenCVLaneCenter:
    """Find white lane boundaries and calculate a local centre correction."""

    def __init__(
        self,
        *,
        max_steering_deg: float = 28.0,
        wheelbase_m: float = 0.26,
        lookahead_m: float = 0.45,
        smoothing_alpha: float = 0.35,
    ) -> None:
        if max_steering_deg <= 0.0:
            raise ValueError("max_steering_deg must be positive")
        if wheelbase_m <= 0.0:
            raise ValueError("wheelbase_m must be positive")
        if lookahead_m <= 0.0:
            raise ValueError("lookahead_m must be positive")
        if not 0.0 < smoothing_alpha <= 1.0:
            raise ValueError("smoothing_alpha must be in (0, 1]")

        self.max_steering_deg = float(max_steering_deg)
        self.wheelbase_m = float(wheelbase_m)
        self.lookahead_m = float(lookahead_m)
        self.smoothing_alpha = float(smoothing_alpha)
        self._offset_px: Optional[float] = None
        self._heading_error_rad: Optional[float] = None
        self._route_offset_px: Optional[float] = None
        self._route_heading_error_rad: Optional[float] = None
        self.last_observation = LaneCenterObservation(
            valid=False,
            center_x_px=None,
            center_offset_px=0.0,
            heading_error_rad=0.0,
            steering_deg=0.0,
            confidence=0.0,
            left_line=None,
            right_line=None,
            mask=None,
            route_centerline_px=None,
        )

    def detect(
        self,
        frame: np.ndarray,
        *,
        visualize: bool = False,
        route_points_px: Optional[np.ndarray] = None,
    ) -> LaneCenterObservation:
        """Estimate the lane centre from a BGR image.

        ``center_offset_px`` is positive when the detected lane centre is to
        the right of the camera centre.  The returned steering correction uses
        the vehicle convention: positive means left.
        """
        if frame is None or not isinstance(frame, np.ndarray):
            return self._invalid_observation(None, None)
        if frame.ndim != 3 or frame.shape[2] != 3 or frame.size == 0:
            return self._invalid_observation(None, None)

        height, width = frame.shape[:2]
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # White lane paint: low saturation and high value.  Keep this mask
        # selective so bonnet reflections and grey map edges are rejected.
        white = cv.inRange(hsv, (0, 0, 160), (180, 100, 255))
        white = cv.morphologyEx(
            white,
            cv.MORPH_CLOSE,
            np.ones((5, 5), dtype=np.uint8),
        )
        edges = cv.Canny(gray, 45, 140)
        # Use edges only where the underlying pixel is lane-like white.  This
        # rejects dark/green bonnet edges that previously generated false
        # Hough lines.
        line_mask = cv.bitwise_or(
            cv.bitwise_and(edges, white),
            cv.Canny(white, 40, 120),
        )

        # The lower part of the simulator image is dominated by the vehicle
        # bonnet. Keep the trapezoid above it and use a narrower top so map
        # borders outside the drivable lane are not treated as lanes.
        roi_top = int(0.30 * height)
        roi_bottom = int(0.90 * height)
        polygon = np.array([[
            (int(0.05 * width), roi_bottom),
            (int(0.95 * width), roi_bottom),
            (int(0.72 * width), roi_top),
            (int(0.28 * width), roi_top),
        ]], dtype=np.int32)
        roi_mask = np.zeros_like(line_mask)
        cv.fillPoly(roi_mask, polygon, 255)
        line_mask = cv.bitwise_and(line_mask, roi_mask)
        # Publish the filled white-paint mask as well as using edge pixels for
        # Hough detection.  This makes the ROS mask useful for tuning instead
        # of showing only a few one-pixel Canny fragments.
        mask = cv.bitwise_and(white, roi_mask)

        lines = cv.HoughLinesP(
            line_mask,
            rho=1.0,
            theta=np.pi / 180.0,
            threshold=max(14, int(0.045 * width)),
            minLineLength=max(20, int(0.10 * height)),
            maxLineGap=max(12, int(0.10 * width)),
        )
        line_candidates = []
        image_center = width / 2.0
        y_near = 0.80 * height
        y_far = 0.44 * height
        route_curve = self._fit_route_curve(
            route_points_px,
            width=width,
            height=height,
            y_far=y_far,
            y_near=y_near,
        )

        if lines is not None:
            for raw_line in lines[:, 0]:
                x1, y1, x2, y2 = map(float, raw_line)
                dy = y2 - y1
                dx = x2 - x1
                if abs(dy) < 1.0 or math.hypot(dx, dy) < 12.0:
                    continue

                slope = dx / dy
                # Horizontal markings and crosswalk bars are rejected.  A
                # lane boundary converges toward the image centre upward.
                if abs(slope) < 0.12 or abs(slope) > 3.0:
                    continue
                intercept = x1 - slope * y1
                x_near = slope * y_near + intercept
                x_far = slope * y_far + intercept
                length = math.hypot(dx, dy)

                # A valid perspective lane line must span a meaningful part
                # of the ROI and converge toward the image centre ahead.
                if abs(y2 - y1) < 0.10 * height:
                    continue
                if not (
                    0.0 * width <= x_near <= 1.0 * width
                    and 0.0 * width <= x_far <= 1.0 * width
                ):
                    continue

                line_candidates.append((
                    slope,
                    intercept,
                    length,
                    x_near,
                    x_far,
                ))

        left_candidates, right_candidates = self._select_lane_pair(
            line_candidates, width)

        left_line = self._weighted_line(left_candidates)
        right_line = self._weighted_line(right_candidates)

        # The centre estimate is intentionally conservative: use both lane
        # boundaries for a valid high-confidence correction.  A single line
        # can still produce a low-confidence correction using the last known
        # lane width, which allows temporary partial occlusions to be bridged.
        lane_width_px = None
        if left_line is not None and right_line is not None:
            left_near = left_line[0] * y_near + left_line[1]
            right_near = right_line[0] * y_near + right_line[1]
            lane_width_px = right_near - left_near
            if lane_width_px < 0.18 * width or lane_width_px > 0.95 * width:
                left_line = None
                right_line = None

        if left_line is None and right_line is None:
            return self._invalid_observation(
                self._draw_debug(
                    frame,
                    polygon,
                    None,
                    None,
                    None,
                    None,
                    route_curve[3] if route_curve is not None else None,
                )
                if visualize else None,
                mask,
                route_curve[3] if route_curve is not None else None,
            )

        if left_line is not None and right_line is not None:
            left_far = left_line[0] * y_far + left_line[1]
            right_far = right_line[0] * y_far + right_line[1]
            left_near = left_line[0] * y_near + left_line[1]
            right_near = right_line[0] * y_near + right_line[1]
            center_far = 0.5 * (left_far + right_far)
            center_near = 0.5 * (left_near + right_near)
            confidence = 1.0
        elif left_line is not None:
            left_far = left_line[0] * y_far + left_line[1]
            left_near = left_line[0] * y_near + left_line[1]
            assumed_width = 0.55 * width
            center_far = left_far + 0.5 * assumed_width
            center_near = left_near + 0.5 * assumed_width
            confidence = 0.35
        else:
            right_far = right_line[0] * y_far + right_line[1]
            right_near = right_line[0] * y_near + right_line[1]
            assumed_width = 0.55 * width
            center_far = right_far - 0.5 * assumed_width
            center_near = right_near - 0.5 * assumed_width
            confidence = 0.35

        center_far = float(np.clip(center_far, -width, 2.0 * width))
        center_near = float(np.clip(center_near, -width, 2.0 * width))
        lane_offset_px = center_far - image_center
        lane_heading_error = math.atan2(
            center_near - center_far,
            y_near - y_far,
        )

        route_centerline = None
        if route_curve is not None:
            route_fit, route_y_mid, route_y_scale, route_centerline = (
                route_curve
            )
            route_far = self._route_x_at(
                route_fit, route_y_mid, route_y_scale, y_far)
            route_near = self._route_x_at(
                route_fit, route_y_mid, route_y_scale, y_near)
            route_heading = math.atan2(
                route_near - route_far,
                y_near - y_far,
            )

            # The planned path is the curved reference. OpenCV contributes
            # only the measured residual from that reference, so a bend is
            # not flattened into two independent straight lines.
            raw_offset_px = (
                0.35 * (center_far - route_far)
                + 0.65 * (center_near - route_near)
            )
            raw_heading_error = lane_heading_error - route_heading
            self._route_offset_px = self._smooth(
                self._route_offset_px, raw_offset_px)
            self._route_heading_error_rad = self._smooth(
                self._route_heading_error_rad, raw_heading_error)
            offset_px = float(self._route_offset_px)
            heading_error = float(self._route_heading_error_rad)
        else:
            self._offset_px = self._smooth(self._offset_px, lane_offset_px)
            self._heading_error_rad = self._smooth(
                self._heading_error_rad, lane_heading_error)
            offset_px = float(self._offset_px)
            heading_error = float(self._heading_error_rad)

        # Convert image displacement to a local pure-pursuit-like correction.
        # The sign is inverted because image x-right is vehicle y-right while
        # the vehicle command convention is positive-left.
        lateral_m = -0.30 * offset_px / max(width / 2.0, 1.0)
        steering_rad = math.atan2(
            2.0 * self.wheelbase_m * lateral_m,
            self.lookahead_m * self.lookahead_m,
        )
        steering_rad += 0.75 * heading_error
        steering_deg = math.degrees(steering_rad)
        if route_curve is not None:
            # The graph controller applies the planned bend. This camera
            # term is only a bounded centre-keeping correction.
            steering_deg *= confidence
            steering_limit = 0.45 * self.max_steering_deg
        else:
            steering_limit = self.max_steering_deg
        steering_deg = float(np.clip(
            steering_deg,
            -steering_limit,
            steering_limit,
        ))

        debug_frame = None
        if visualize:
            debug_frame = self._draw_debug(
                frame,
                polygon,
                left_line,
                right_line,
                center_far,
                center_near,
                route_centerline,
            )

        observation = LaneCenterObservation(
            valid=True,
            center_x_px=center_far,
            center_offset_px=offset_px,
            heading_error_rad=heading_error,
            steering_deg=steering_deg,
            confidence=confidence,
            left_line=left_line,
            right_line=right_line,
            mask=mask,
            debug_frame=debug_frame,
            route_centerline_px=route_centerline,
        )
        self.last_observation = observation
        return observation

    @staticmethod
    def _fit_route_curve(route_points_px, *, width, height, y_far, y_near):
        """Fit a smooth image-space curve to the projected graph path."""
        if route_points_px is None:
            return None
        points = np.asarray(route_points_px, dtype=float)
        if points.ndim != 2 or points.shape[1] != 2 or len(points) < 3:
            return None
        valid = np.isfinite(points).all(axis=1)
        valid &= points[:, 0] >= -0.5 * width
        valid &= points[:, 0] <= 1.5 * width
        valid &= points[:, 1] >= 0.25 * height
        valid &= points[:, 1] <= 0.92 * height
        points = points[valid]
        if len(points) < 3:
            return None

        # Never extrapolate a route that is visible only at the horizon. That
        # was producing a false magenta line at the bottom of the image and
        # could pull the car toward a side lane. Require the projected path to
        # span most of the steering window before using it as a reference.
        if (
            np.min(points[:, 1]) > y_far + 0.15 * height
            or np.max(points[:, 1]) < y_near - 0.10 * height
        ):
            return None

        # Perspective projection can collapse dense path samples onto one
        # image row. Remove repeated rows before fitting the polynomial.
        points = points[np.argsort(points[:, 1])]
        _, unique_indices = np.unique(
            np.round(points[:, 1], 2), return_index=True)
        points = points[unique_indices]
        if len(points) < 3:
            return None

        y_mid = 0.5 * (y_far + y_near)
        y_scale = max(0.5 * (y_near - y_far), 1.0)
        y_normalized = (points[:, 1] - y_mid) / y_scale
        degree = min(3, len(points) - 1)
        fit = np.polynomial.Polynomial.fit(
            y_normalized,
            points[:, 0],
            deg=degree,
        )
        sample_y = np.linspace(y_far, y_near, 24)
        sample_x = fit((sample_y - y_mid) / y_scale)
        centerline = np.column_stack((sample_x, sample_y)).astype(np.float32)
        return fit, y_mid, y_scale, centerline

    @staticmethod
    def _route_x_at(route_fit, y_mid, y_scale, y):
        return float(route_fit((float(y) - y_mid) / y_scale))

    @staticmethod
    def _weighted_line(candidates):
        if not candidates:
            return None
        weights = np.asarray([line[2] for line in candidates], dtype=float)
        values = np.asarray([[line[0], line[1]] for line in candidates], dtype=float)
        slope, intercept = np.average(values, axis=0, weights=weights)
        return float(slope), float(intercept)

    @classmethod
    def _select_lane_pair(cls, candidates, width):
        """Select two ordered lane boundaries by geometry, not slope sign."""
        if len(candidates) < 2:
            return (
                [(c[0], c[1], c[2]) for c in candidates if c[3] < width / 2.0],
                [(c[0], c[1], c[2]) for c in candidates if c[3] >= width / 2.0],
            )

        best_pair = None
        best_score = -float('inf')
        image_center = width / 2.0
        for left in candidates:
            for right in candidates:
                if left is right or left[3] >= right[3]:
                    continue

                near_width = right[3] - left[3]
                far_width = right[4] - left[4]
                if not (0.18 * width <= near_width <= 0.85 * width):
                    continue
                if not (0.05 * width <= far_width <= 0.75 * width):
                    continue

                near_center = 0.5 * (left[3] + right[3])
                far_center = 0.5 * (left[4] + right[4])
                if not (0.05 * width <= far_center <= 0.95 * width):
                    continue

                # Prefer long, well-separated lines and mildly prefer a lane
                # centre near the optical centre without forcing it there.
                score = (
                    left[2] + right[2]
                    - 0.35 * abs(near_width - 0.45 * width)
                    - 0.10 * abs(far_center - image_center)
                    - 0.10 * abs(near_center - image_center)
                )
                if score > best_score:
                    best_score = score
                    best_pair = (left, right)

        if best_pair is None:
            return (
                [(c[0], c[1], c[2]) for c in candidates if c[3] < image_center],
                [(c[0], c[1], c[2]) for c in candidates if c[3] >= image_center],
            )

        left, right = best_pair
        return (
            [(left[0], left[1], left[2])],
            [(right[0], right[1], right[2])],
        )

    def _smooth(self, previous, current):
        if previous is None:
            return float(current)
        alpha = self.smoothing_alpha
        return float(alpha * current + (1.0 - alpha) * previous)

    def _invalid_observation(self, debug_frame, mask, route_centerline=None):
        observation = LaneCenterObservation(
            valid=False,
            center_x_px=None,
            center_offset_px=0.0,
            heading_error_rad=0.0,
            steering_deg=0.0,
            confidence=0.0,
            left_line=None,
            right_line=None,
            mask=mask,
            debug_frame=debug_frame,
            route_centerline_px=route_centerline,
        )
        self.last_observation = observation
        return observation

    @staticmethod
    def _draw_debug(
        frame,
        polygon,
        left_line,
        right_line,
        center_far,
        center_near,
        route_centerline=None,
    ):
        debug = frame.copy()
        cv.polylines(debug, polygon, True, (255, 255, 0), 2)
        height, width = debug.shape[:2]
        y_near = int(0.80 * height)
        y_far = int(0.44 * height)
        if route_centerline is not None:
            route_points = np.asarray(route_centerline, dtype=np.float32)
            route_points = route_points[
                np.isfinite(route_points).all(axis=1)]
            if len(route_points) >= 2:
                cv.polylines(
                    debug,
                    [np.round(route_points).astype(np.int32)],
                    False,
                    (255, 0, 255),
                    3,
                    cv.LINE_AA,
                )
        for line, color in ((left_line, (255, 0, 0)), (right_line, (0, 0, 255))):
            if line is None:
                continue
            slope, intercept = line
            x_far = int(slope * y_far + intercept)
            x_near = int(slope * y_near + intercept)
            cv.line(debug, (x_far, y_far), (x_near, y_near), color, 3)
        if center_far is not None and center_near is not None:
            cv.line(
                debug,
                (int(center_far), y_far),
                (int(center_near), y_near),
                (0, 255, 0),
                3,
            )
        cv.line(debug, (width // 2, y_far), (width // 2, y_near), (0, 255, 255), 2)
        return debug


class OpenCVLaneImagePublisher:
    """Publish the detector overlay and binary lane mask as ROS images."""

    def __init__(
        self,
        node,
        *,
        overlay_topic: str = '/brain/opencv_lane_center/overlay',
        mask_topic: str = '/brain/opencv_lane_center/mask',
    ) -> None:
        self._node = node
        self._bridge = CvBridge()
        self._overlay_pub = node.create_publisher(Image, overlay_topic, 1)
        self._mask_pub = node.create_publisher(Image, mask_topic, 1)

    def publish(self, observation: LaneCenterObservation, frame=None) -> None:
        """Publish the latest overlay and mask, if image data is available."""
        overlay = observation.debug_frame
        if overlay is None:
            overlay = frame
        if overlay is not None:
            overlay_msg = self._bridge.cv2_to_imgmsg(
                np.ascontiguousarray(overlay), encoding='bgr8')
            self._stamp(overlay_msg)
            self._overlay_pub.publish(overlay_msg)

        if observation.mask is not None:
            mask = np.asarray(observation.mask, dtype=np.uint8)
            mask_msg = self._bridge.cv2_to_imgmsg(
                np.ascontiguousarray(mask), encoding='mono8')
            self._stamp(mask_msg)
            self._mask_pub.publish(mask_msg)

    def _stamp(self, message: Image) -> None:
        message.header.stamp = self._node.get_clock().now().to_msg()
        message.header.frame_id = 'oak_rgb_camera_frame'


def fuse_route_and_lane_steering(
    route_steering_deg: float,
    lane_steering_deg: float,
    lane_confidence: float,
    *,
    max_steering_deg: float = 28.0,
) -> float:
    """Blend local lane-centre steering into the global route command.

    The route command remains dominant during large turns, where camera lane
    markings can be ambiguous.  On straights, a visible lane centre supplies
    most of the correction for lateral drift.
    """
    values = (route_steering_deg, lane_steering_deg, lane_confidence)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("steering and confidence values must be finite")
    if max_steering_deg <= 0.0:
        raise ValueError("max_steering_deg must be positive")

    confidence = float(np.clip(lane_confidence, 0.0, 1.0))
    turn_factor = max(
        0.15,
        1.0 - abs(route_steering_deg) / max_steering_deg,
    )
    lane_weight = 0.55 * confidence * turn_factor
    fused = (
        (1.0 - lane_weight) * route_steering_deg
        + lane_weight * lane_steering_deg
    )
    return float(np.clip(fused, -max_steering_deg, max_steering_deg))
