# GET POSITION BY CLICKING ON THE MAP
# then save it in the variable event_points.npy, aleady in R coord

import numpy as np
import cv2 as cv
import os
import helper_functions as hf

wind_name = 'Get position'
event_points = []

def mouse_callback(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        # cv.circle(img, (x,y), 50, (0,200,0), 10)
        p_pix = np.array([x,y])
        p = hf.pix2mR(p_pix)
        p[0] = round(p[0],2)
        p[1] = round(p[1],2)
        print(p)
        event_points.append(p)
        cv.circle(img, hf.mR2pix(p), 50, (200,0,200), 10)
        cv.circle(img, hf.mR2pix(p), 3, (200,0,200), -1)
        cv.putText(img, str(p), hf.mR2pix(p), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2)

img = cv.imread('data/2024_VerySmall.png')
cv.namedWindow(wind_name, cv.WINDOW_NORMAL)
cv.imshow(wind_name, img)

cv.setMouseCallback(wind_name, mouse_callback)

while True:
    cv.imshow(wind_name, img)
    key = cv.waitKey(1) 
    if key == 27: #ESC
        print('Exiting...')
        break


cv.destroyAllWindows()