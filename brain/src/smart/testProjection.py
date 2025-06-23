#!/usr/bin/env python3
import numpy as np
from collections import deque
import cv2
import time
import helper_functions as hf
from path_planning4_mod import PathPlanning

# Initialize path planner
map_img = cv2.imread('data/2024_VerySmall.png')
path_planner = PathPlanning(map_image)
path_planner.compute_shortest_path(source=125, target=401)

# Path data
path = np.array(self.path_planner.get_path())

print("Path found:", path)
