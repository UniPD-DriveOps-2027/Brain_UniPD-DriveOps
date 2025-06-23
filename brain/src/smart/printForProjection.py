#!/usr/bin/env python3
import numpy as np
from collections import deque
import cv2
import time
#import helper_functions as hf
from path_planning4_mod import PathPlanning
#from automobile_data_pi import AutomobileDataPi



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
