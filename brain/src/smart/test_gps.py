from names_and_constants import SIMULATOR_FLAG, SHOW_IMGS, RANDOM_START, EVENT_SETTINGS, EVENT_CONFIGS, ARENA, RESUME# deleted completely the speed challenge
import sys
import os
import numpy as np
import cv2 as cv
from time import time, sleep
from numpy.linalg import norm
from collections import deque
import names_and_constants as nac
from extra.giveme_fruits import compute_optimal_path
import math

if not SIMULATOR_FLAG:
    from automobile_data_interface import Automobile_Data
else:
    from automobile_data_interface import Automobile_Data
    
from path_planning4_mod import PathPlanning
from controller3 import Controller
from controllerSP import ControllerSpeed
from controllerAG import ControllerSpeed as ControllerBL
from detection import Detection
from environmental_data_simulator import EnvironmentalData
from obstacle2 import Obstacle
import helper_functions as hf

STARTING_COORDS = [2.79, 6.1] # GET FROM GPS 
CHECKPOINTS = compute_optimal_path(start_node=472) # GET FROM FRUITS
END_NODE = CHECKPOINTS[-1]  #get the last node from the path
YAW_OFFSET = 180
class TestGps:
    def __init__(self,
                 car: Automobile_Data,
                 path_planner: PathPlanning
                 ):
        self.path_planner = path_planner
        self.car = car
        curr_time = time()
    def clos_node(self, curr_pos):
        #curr_pos = np.array([self.car.x_est, self.car.y_est]) 
        closest_node, distance = self.path_planner.get_closest_node_start(curr_pos, self.car.yaw+YAW_OFFSET)
        return closest_node
    
if __name__ == "__main__":
    from automobile_data_pi import AutomobileDataPi
    # init trajectory
    track = cv.imread('data/2024_VerySmall.png')
    path_planner = PathPlanning(track)
    # init env
    car = AutomobileDataPi(trig_cam=False,
                           trig_gps=False,
                           trig_bno=True, 
                           trig_enc=True,
                           trig_control=True,
                           trig_sonar=True,
                           trig_lidar=True,
                           trig_tof=True)
    env = EnvironmentalData(trig_v2v=True, trig_v2x=True, trig_semaphore=True)
    gps_node = TestGps(car=car, path_planner=path_planner)

    try:
        while True:
            pos = STARTING_COORDS
            node = gps_node.clos_node(pos)
            print(f"Closest node: {node}")
            sleep(0.5)  # optional: to avoid excessive CPU usage
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting cleanly...")
        # Optionally do cleanup here
        sys.exit(0)
