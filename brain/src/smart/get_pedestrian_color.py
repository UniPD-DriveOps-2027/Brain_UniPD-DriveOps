#!/usr/bin/python3
import sys
import os

# Get the parent directory of the current script
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent directory to sys.path
sys.path.insert(0, parent_dir)

import signal
import cv2 as cv
import rospy                # type: ignore #suppress warning
import numpy as np
from time import sleep, time
from unix_socket_camera import UnixSocketCamera

import json
with open('data/events_config.json', 'r') as file:
    events_config = json.load(file)


from automobile_data_pi import AutomobileDataPi

import names_and_constants as nac    
import helper_functions as hf
from path_planning4 import PathPlanning
from controller3 import Controller
from controllerSP import ControllerSpeed
from controllerAG import ControllerSpeed as ControllerBL
from detection import Detection
from brain import Brain
from rc_brain import RC_Brain
from environmental_data_simulator import EnvironmentalData


os.system('clear')
print('Test starting...')

track = cv.imread('../data/2024_VerySmall.png')

# PARAMETERS
TARGET_FPS = 30.0 # target fps of the main loop

DESIRED_SPEED = 0.35  # [m/s]
SP_SPEED = 0.35  # [m/s]
CURVE_SPEED = 0.25  # [m/s]
BL_SP_SPEED = 0.8
BL_CURVE_SPEED = 0.5

# CONTROLLER
k1 = 0.0  # 0.0 gain error parallel to direction (speed)
k2 = 0.0  # 0.0 perpenddicular error gain
k3_NL = 1.3 # for no_lane part #BFMC_2024
k3 = 1.0 # rest of the map #BFMC_2024
k3D = 0.08  # 0.08 derivative gain of yaw error
dist_point_ahead = 0.35  # distance of the point ahead in m

ff_curvature = 1.0  # feedforward gain

x_orig = 0.0
y_orig = 0.0

cap = UnixSocketCamera(socket_addr="/tmp/bfmc_camera_brain.sock", frame_size=(320, 240))


# stop the car with ctrl+c
def handler(signum, frame):
    print("Exiting ...")
    car.stop()
    cv.destroyAllWindows()
    sleep(.99)
    exit()

nac.TESTING = True
nac.DRIVE_DESIRED_SPEED = 0.3


if __name__ == '__main__':

    hf.create_frames(nac.SHOW_IMGS)

    car = AutomobileDataPi(trig_cam=False,
                               trig_gps=True,
                               trig_bno=True, 
                               trig_enc=True,
                               trig_control=True,
                               trig_sonar=True,
                               trig_lidar=True) 
    sleep(1.5)

    signal.signal(signal.SIGINT, handler)

    # init trajectory
    path_planner = PathPlanning(track)

    # init env
    env = EnvironmentalData(trig_v2v=True, trig_v2x=True, trig_semaphore=True)

    # init controller
    controller = Controller(k1=k1, k2=k2, k3=k3, k3_NL=k3_NL, k3D=k3D,
                            dist_point_ahead=dist_point_ahead,
                            ff=ff_curvature)
    controller_sp = ControllerSpeed(desired_speed=SP_SPEED,
                                    curve_speed=CURVE_SPEED)
    controller_ag = ControllerBL(straight_speed=BL_SP_SPEED,
                                 curve_speed=BL_CURVE_SPEED,
                                 lookahead=0.8)

    # initiliaze all the neural networks for detection and lane following
    detect = Detection()

    brain = Brain(car=car, controller=controller, controller_sp=controller_sp,
                        controller_ag=controller_ag,
                        detection=detect, env=env, path_planner=path_planner,
                        desired_speed=DESIRED_SPEED)
    
    
    hf.show_track(track, car, nac.SHOW_IMGS)

    try:
        car.stop()
        fps_avg = 0.0
        fps_cnt = 0
        while not rospy.is_shutdown():

            loop_start_time = time()
            # clear the screen
            #print("\033c")
            
            # <++++++++++++++++++++>
            hf.show_car(track, car, nac.SHOW_IMGS)

            ret, frame = cap.read()
            if not ret:
                print("No image from Unix socket camera")
                frame = np.zeros((240, 320, 3), np.uint8)
                continue
            brain.car.frame = frame
            

            hf.show_camera(car, nac.SHOW_IMGS)

            cv.namedWindow("click_to_get_hsv")
            cv.setMouseCallback("click_to_get_hsv", mouse_callback, param=frame)

            if nac.SHOW_IMGS:
                if cv.waitKey(1) == 27:
                    cv.destroyAllWindows()
                    break

            loop_time = time() - loop_start_time
            fps_avg = (fps_avg * fps_cnt + 1.0 / loop_time) / (fps_cnt + 1)
            fps_cnt += 1
            if loop_time < 1.0 / TARGET_FPS:
                sleep(1.0 / TARGET_FPS - loop_time)

    except KeyboardInterrupt:
        print("Shutting down")
        car.stop()
        sleep(.5)
        cv.destroyAllWindows()
        exit(0)
    except rospy.ROSInterruptException:
        pass


    clicked_hsv_values = []

def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        frame = param
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Define the size of the region around the click (e.g., 5x5)
        region_size = 5
        half_size = region_size // 2

        x_start = max(0, x - half_size)
        y_start = max(0, y - half_size)
        x_end = min(frame.shape[1], x + half_size + 1)
        y_end = min(frame.shape[0], y + half_size + 1)

        # Extract the region of interest
        roi = hsv_frame[y_start:y_end, x_start:x_end]

        # Compute min and max HSV in the region
        h_min, s_min, v_min = np.min(roi[:, :, 0]), np.min(roi[:, :, 1]), np.min(roi[:, :, 2])
        h_max, s_max, v_max = np.max(roi[:, :, 0]), np.max(roi[:, :, 1]), np.max(roi[:, :, 2])

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        clicked_hsv_values.append((lower, upper))

        print(f"HSV range from ({x},{y}) in a {region_size}x{region_size} area:")
        print(f"  Lower: {lower}")
        print(f"  Upper: {upper}")
