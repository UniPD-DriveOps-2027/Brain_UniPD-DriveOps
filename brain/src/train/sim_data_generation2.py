DS_NAME, CHECKPOINTS = 'left', [(100,122), (113, 95)]
# DIST_POINT_AHEAD = 0.35 # distance of the point ahead
DIST_POINT_AHEAD = 0.45 # distance of the point ahead
LAPS = 1


import os, signal
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from time import sleep, time
from stuff import *
from tqdm import tqdm # progress bar

imgs, alphas = [], [] # input and label of the dataset
IPA = int(100*DIST_POINT_AHEAD) # IPA=index point ahead, the path is sampled every 1[cm]

STEER_NOSIE_STDS_DEG = np.linspace(0, 20, 11)
POSITION_NOISE_STD = np.linspace(0, 0.1, 11)
# OPTIMAL_IDX = 6 #to select steering noise std and position noise std, check my thesis
OPTIMAL_IDX = 0 #set to 0 to not get an epileptic attack
sn_std, pos_std = STEER_NOSIE_STDS_DEG[OPTIMAL_IDX], POSITION_NOISE_STD[OPTIMAL_IDX]
print(f'noise std: {sn_std}, pos std: {pos_std}')

file_name = 'training_dss/sim_ds_'
if not os.path.exists('training_dss'): os.makedirs('training_dss')

TARGET_FPS = 30
    

# ## create path
cv.namedWindow('Path', cv.WINDOW_NORMAL)
cv.setWindowProperty('Path', 2*1920, 2*1080)
cv.namedWindow('Frame', cv.WINDOW_NORMAL)
cv.setWindowProperty('Frame', 1920, 1080)

from path_planning import PathPlanning
pp = PathPlanning()
epath = [] 
for cp1, cp2 in CHECKPOINTS:
    #compute path between checkpoints
    traj = pp.compute_shortest_path(source=cp1, target=cp2)
    xs, ys = traj[:,0], traj[:,1]
    #create yaw sequence
    yaws = np.zeros(len(traj))
    for i in range(len(traj)-1):
        yaws[i] = np.arctan2(ys[i+1]-ys[i], xs[i+1]-xs[i])
    yaws[-1] = yaws[-2] # last yaw is the same as the second last
    # keep only the first part of the path (skip the last IPA points)
    xs, ys, yaws = xs[:-IPA], ys[:-IPA], yaws[:-IPA]
    xpas, ypas = traj[IPA:,0], traj[IPA:,1]
    assert len(xs) == len(ys) == len(yaws) == len(xpas) == len(ypas), f'{len(xs)}, {len(ys)}, {len(yaws)}, {len(xpas)}, {len(ypas)}'

    # add noise
    y_errors, yaw_errors = np.random.normal(0, pos_std, len(xs)), np.random.normal(0, np.deg2rad(sn_std), len(xs))
    for i in range(len(xs)):
        xp, yp, yawp = xs[i], ys[i], yaws[i]
        y_error, yaw_error = y_errors[i], yaw_errors[i]
        e = np.array([0, y_error])
        R = np.array([[np.cos(yawp), -np.sin(yawp)], [np.sin(yawp), np.cos(yawp)]])
        e = R @ e # rotate error
        xs[i] = xp + e[0]
        ys[i] = yp + e[1]
        yaws[i] = yawp + yaw_error

    # calculate alphas
    αs = np.zeros(len(xs))
    for i in range(len(xs)):
        x1, y1 = xs[i], ys[i]
        x2, y2 = xpas[i], ypas[i]
        dx, dy = x2-x1, y2-y1
        αs[i] = diff_angle(np.arctan2(dy, dx), yaws[i])

    #add path to list
    epath.append(np.vstack((xs, ys, yaws, αs)).T)
    #draw path
    pp.draw_path()

epath = np.vstack(epath)
print(f'epath shape: {epath.shape}')


cv.imshow('Path', cv.flip(pp.map, 0))
cv.waitKey(1)




#concatenate path with itself to make it longer based on LAPS
epath = np.tile(epath, (LAPS,1))

#decimate path
# epath = epath[::12]

map = load_map()

#initializations
os.system('rosservice call /gazebo/reset_simulation') 
os.system('rosrun example visualizer.py &') #run visualization ncode

#car placement in simulator
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
ros.wait_for_service('/gazebo/set_model_state')
state_msg = ModelState()
state_msg.model_name = 'automobile'
state_msg.pose.position.x = 0
state_msg.pose.position.y = 0
state_msg.pose.position.z = 0.032939
state_msg.pose.orientation.x = 0
state_msg.pose.orientation.y = 0
state_msg.pose.orientation.z = 0
state_msg.pose.orientation.w = 0
def place_car(x,y,yaw):
    state_msg.pose.position.x = x
    state_msg.pose.position.y = y
    state_msg.pose.orientation.z = np.sin(yaw/2)
    state_msg.pose.orientation.w = np.cos(yaw/2)
    set_state = ros.ServiceProxy('/gazebo/set_model_state', SetModelState)
    _ = set_state(state_msg)
    sleep(0.02)

def save_data(imgs,locs,alphas, name):
    imgs = np.array(imgs)
    locs = np.array(locs)
    alphas = np.array(alphas)
    np.savez_compressed(name, imgs=imgs, locs=locs, alphas=alphas)
    print(f'saved data to {name}')
    # print('not saving, testing')

frame = None
bridge = CvBridge()

ros.init_node('gazebo_move')
def camera_callback(data) -> None:
    """Receive and store camera frame
    :acts on: self.frame
    """        
    global frame, bridge
    frame = bridge.imgmsg_to_cv2(data, "bgr8")

camera_sub = ros.Subscriber('/automobile/image_raw', Image, camera_callback)

ds_path = f'{file_name}{DS_NAME}_sn{sn_std:.2f}.npz'

sleep(0.9)

LAP_Y_TRSH = 2.54 + 2.5
START_X = 5.03
START_Y = LAP_Y_TRSH
START_YAW = np.deg2rad(90.0) + π

while frame is None:
    print('waiting for frame, is ros running?')
    sleep(0.1)

for i in tqdm(range(len(epath))):
    loop_start = time()
    x,y,yaw,α = epath[i]

    #place car
    place_car(x,y,yaw)

    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (320, 240), interpolation=cv.INTER_AREA)
    imgs.append(img)
    alphas.append(α)

    tmp_frame = frame.copy() #copy frame to draw on
    
    xpa, ypa = x + DIST_POINT_AHEAD*np.cos(yaw+α), y + DIST_POINT_AHEAD*np.sin(yaw+α)

    proj_point = project_onto_frame(np.array([xpa, ypa]), cp=Pose(x, y, yaw))
    cv.circle(tmp_frame, (int(proj_point[0]), int(proj_point[1])), 5, (0, 255, 0), -1)

    # show image
    cv.imshow('Frame', tmp_frame)
    # cv.imshow('Path', pp.map)



    #calculate fps
    loop_time = time() - loop_start
    fps = 1.0 / loop_time
    # print(f'NOISE: {sn_std}')
    # print(f'x: {x:.2f}, y: {y:.2f}, yaw: {np.rad2deg(yaw):.2f}, fps: {fps:.2f}')

    if cv.waitKey(1) == 27:
        print('ESC pressed, exiting')
        cv.destroyAllWindows()
        exit(0)

    if loop_time < 1/TARGET_FPS:
        sleep(1/TARGET_FPS - loop_time)

save_data(imgs, locs, ds_path)

cv.destroyAllWindows()



