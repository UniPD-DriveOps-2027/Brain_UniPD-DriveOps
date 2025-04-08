# test the network
from he_train import NET_PATH, IMG_SIZE, DIST_POINT_AHEAD, INFERENCE_FLIP, preprocess_image
import cv2 as cv

from stuff import *
from time import time, sleep
import numpy as np, os

os.system('rosservice call /gazebo/pause_physics') #pause physics
os.system('rosservice call /gazebo/reset_simulation') #reset simulation
os.system('rosservice call /gazebo/unpause_physics') #unpause physics

FPS = 15.0
TARGET_SPEED = .5
KP = 1.3 # "proportional gain"

#run visualization node
os.system('rosrun example visualizer.py &')

#camera
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String
import json
frame = None
bridge = CvBridge()
ros.init_node('he_test')
def camera_callback(data) -> None:
    """Receive and store camera frame
    :acts on: self.frame
    """        
    global frame, bridge
    frame = bridge.imgmsg_to_cv2(data, "bgr8")
camera_sub = ros.Subscriber('/automobile/image_raw', Image, camera_callback)
# drive
drive_sub = ros.Publisher('/automobile/command', String, queue_size=2)
def drive(speed, angle):
    drive_sub.publish(json.dumps({'action': '1', 'speed': float(speed)}))
    drive_sub.publish(json.dumps({'action': '2', 'steerAngle': float(np.rad2deg(angle))}))

#load network
net = cv.dnn.readNetFromONNX(NET_PATH)

cv.namedWindow('frame', cv.WINDOW_NORMAL)
cv.resizeWindow('frame', 640, 480)
cv.namedWindow('preprocessed', cv.WINDOW_NORMAL)
cv.resizeWindow('preprocessed', 240, 240)

while not ros.is_shutdown():
    try:
        start = time()
        #get camera image
        while frame is None:
            sleep(0.1)
        img = frame.copy()
        tmp_frame = frame.copy()
        img = preprocess_image(img)
        if INFERENCE_FLIP:
            img_flip = cv.flip(img, 1)
            imgs = np.stack((img, img_flip), axis=0)
        else: 
            imgs = np.stack((img, img), axis=0)
        blob = cv.dnn.blobFromImages(imgs, 1.0, (IMG_SIZE, IMG_SIZE), 0, swapRB=True, crop=False)
        net.setInput(blob)
        out = net.forward()
        if INFERENCE_FLIP:
            α, α_flip = out[0][0], out[1][0]
            α = (α - α_flip) / 2
        else:
            α = out[0][0]

        print(f'α -> {np.rad2deg(α):.1f}°        ', end='\r')

        #drive
        drive(TARGET_SPEED, -KP*α) # extremely simple P controller

        #draw
        # tmp_frame = cv.resize(tmp_frame, (2*IMG_SIZE, 2*IMG_SIZE))
        # tmp_frame = cv.cvtColor(tmp_frame, cv.COLOR_BGR2RGB)
        pa = np.array([DIST_POINT_AHEAD*np.cos(α), DIST_POINT_AHEAD*np.sin(α)])
        ppa = project_onto_frame(pa)
        cv.circle(tmp_frame, ppa, 5, (255, 0, 255), -1)
        cv.line(tmp_frame, (320//2, 240), ppa, (255, 0, 255), 2)
        cv.imshow('frame', tmp_frame)
        cv.imshow('preprocessed', img)
        if cv.waitKey(1) == 27: raise Exception('ESC pressed')

        #wait for next frame
        end = time()
        sleep(max(0, (1/FPS) - (end-start)))
    except Exception as e:
        print(e)
        drive(0, 0)
        os.system('rosservice call /gazebo/reset_simulation')
        cv.destroyAllWindows()
        sleep(0.5)
        print('Exiting...')
        break
