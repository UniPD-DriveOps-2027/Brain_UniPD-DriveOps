#!/usr/bin/env python3
import numpy as np
from collections import deque
import cv2
import time
#import helper_functions as hf
from path_planning4_mod import PathPlanning
#from automobile_data_pi import AutomobileDataPi


class SimulatedPathTracker:
    def __init__(self, map_image, start_node, end_node, display_scale=0.5):
        """
        Path tracker with simulated distance input
        
        Args:
            map_image: Loaded map image (cv2 format)
            start_node: Starting node ID
            end_node: Target node ID
        """
        self.display_scale = display_scale
        self.visited_positions = []

        # Initialize path planner
        self.path_planner = PathPlanning(map_image)
        self.path_planner.compute_shortest_path(source=start_node, target=end_node)
        
        # Path data
        self.path = np.array(self.path_planner.get_path())
        self.segment_lengths = np.linalg.norm(np.diff(self.path, axis=0), axis=1)
        self.cumulative_dist = np.cumsum(self.segment_lengths)
        self.total_length = self.cumulative_dist[-1] if len(self.cumulative_dist) > 0 else 0


        # Tracking state
        self.current_index = 0
        self.distance_traveled = 0
        self.position_buffer = deque(maxlen=5)  # Smoothing buffer
        self.last_update_time = time.time()
        self.current_speed = 0  # m/s
        
        print(f"Simulated tracker ready | Path length: {self.total_length:.2f}m")

    def update_from_distance(self, distance, current_yaw_deg=None):
        current_time = time.time()
        dt = current_time - self.last_update_time
        self.current_speed = distance / dt if dt > 0 else 0
        self.last_update_time = current_time

        self.distance_traveled += distance

        best_idx = self._find_by_distance(self.distance_traveled)

        self.position_buffer.append(best_idx)
        self.current_index = int(np.median(self.position_buffer))

        pos_pixel = self._to_pixels(self.path[self.current_index])

        # Add small Gaussian noise to position
        noise_stddev = 3  # pixels
        noisy_pixel = (
            int(pos_pixel[0] + np.random.normal(0, noise_stddev)),
            int(pos_pixel[1] + np.random.normal(0, noise_stddev))
        )
        self.visited_positions.append(noisy_pixel)

        # Optional: limit trail length
        MAX_TRAIL_LENGTH = 500
        if len(self.visited_positions) > MAX_TRAIL_LENGTH:
            self.visited_positions.pop(0)

        if self.distance_traveled >= self.total_length:
            self.distance_traveled = self.total_length
            self.current_index = len(self.path) - 1

        return self.path[self.current_index], self.current_index


    def _find_by_distance(self, distance):
        # distance here should be total distance traveled from path start, not incremental distance
        total_dist = min(distance, self.total_length)
        return np.argmin(np.abs(self.cumulative_dist - total_dist))


    def visualize(self, map_img, show_info=True):
        """Draw path and current position with optional info"""
        display_img = map_img.copy()

        # Draw path
        path_pixels = [self._to_pixels(p) for p in self.path]
        cv2.polylines(display_img, [np.array(path_pixels)], False, (0,200,200), 3)

        # Draw trail with rainbow colors BEFORE scaling
        for i, pt in enumerate(self.visited_positions):
            hue = int(180 * i / max(1, len(self.visited_positions)))  # OpenCV hue: 0-179
            color = cv2.cvtColor(np.uint8([[[hue, 255, 255]]]), cv2.COLOR_HSV2BGR)[0, 0].tolist()
            cv2.circle(display_img, pt, 10, color, -1)

        # Draw current position
        if self.current_index < len(self.path):
            pos = self.path[self.current_index]
            pos_pixel = self._to_pixels(pos)
            cv2.circle(display_img, pos_pixel, 12, (0,0,255), -1)
            cv2.circle(display_img, pos_pixel, 16, (255,255,255), 3)

            # Draw direction indicator
            if self.current_index < len(self.path)-1:
                next_pos = self.path[self.current_index+1]
                next_pixel = self._to_pixels(next_pos)
                cv2.arrowedLine(display_img, pos_pixel, next_pixel, (0,255,0), 2)

        # Draw info overlay
        if show_info:
            progress = 100 * (self.distance_traveled / self.total_length)
            info_text = [
                f"Position: {pos[0]:.2f}, {pos[1]:.2f}",
                f"Segment: {self.current_index}/{len(self.path)}",
                f"Progress: {progress:.1f}%",
                f"Speed: {self.current_speed:.2f}m/s",
                f"length cumulative_dist: {len(self.cumulative_dist):.2f}"
            ]
            for i, text in enumerate(info_text):
                cv2.putText(display_img, text, (10, 60 + i*60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 7)

        # Now scale down image for display
        if self.display_scale != 1.0:
            display_img = cv2.resize(display_img, (0, 0), fx=self.display_scale, fy=self.display_scale)

        return display_img



    def _to_pixels(self, point):
        """Convert metric coordinates to pixels (adjust scale/offset as needed)"""

        return (hf.mR2pix(point))


if __name__ == "__main__":
    # Load map and initialize
    map_img = cv2.imread('data/2024_VerySmall.png')
    tracker = SimulatedPathTracker(map_img, start_node=460, end_node=334, display_scale=0.25)

    # Initialize car data interface
    from automobile_data_pi import AutomobileDataPi
    car = AutomobileDataPi(trig_cam=False,
                           trig_gps=False,
                           trig_bno=False, 
                           trig_enc=False,
                           trig_control=False,
                           trig_sonar=False,
                           trig_lidar=False,
                           trig_tof=False)

    # Wait for encoder to initialize
    print("Waiting for encoder data...")
    while car.encoder_distance is None:
        time.sleep(0.1)

    print("Encoder ready. Starting tracking.")

    # Set initial offset and last position
    last_encoder_distance = car.encoder_distance

    while True:
        current_encoder_distance = car.encoder_distance
        incremental_distance = current_encoder_distance - last_encoder_distance
        last_encoder_distance = current_encoder_distance
        print(f"Incremental distance: {incremental_distance}")

        # Update only if movement happened (optional safety)
        if incremental_distance > 0:
            position, idx = tracker.update_from_distance(incremental_distance)

        # Visualization
        display = tracker.visualize(map_img)
        cv2.imshow('Path Tracking Simulation', display)

        # Break if window is closed or 'q' is pressed
        key = cv2.waitKey(10) & 0xFF
        if key == ord('q'):
            break
        if cv2.getWindowProperty('Path Tracking Simulation', cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()
    print(f"Tracking completed. Final position: {position}")


map_img = cv2.imread('data/2024_VerySmall.png')
CHECKPOINTS = [468, 393, 306, 150, 140, 121, 92, 109, 130, 147, 175, 133, 123, 118, 91, 163, 373, 406, 444]
path_planner = PathPlanning(map_img)

# Accumulate paths here as list of arrays
paths_list = []

for i in range(len(CHECKPOINTS) - 1):
    start_node = CHECKPOINTS[i]
    end_node = CHECKPOINTS[i + 1]
    path_planner.compute_shortest_path(source=start_node, target=end_node)
    sub_path = path_planner.get_path()  # Assume shape (m, 2)
    paths_list.append(sub_path)

# Concatenate all sub-paths into one big path array
path = np.vstack(paths_list)

# Remove consecutive duplicate points safely
filtered_path = [path[0]]  # Start with first point
for i in range(1, len(path)):
    if not np.array_equal(path[i], path[i-1]):
        filtered_path.append(path[i])
filtered_path = np.array(filtered_path)

# Save filtered_path to a .npy file for easy loading in other Python scripts
np.savetxt('testProjectionPath.csv', filtered_path, delimiter=',')
