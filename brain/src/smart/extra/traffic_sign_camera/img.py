import cv2
from picamera2 import Picamera2
import time
import os

cpt = 0
maxFrames = 50
save_dir = "/home/eugen/Desktop/traffic_sign_camera/images"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

picam2 = Picamera2()
picam2.preview_configuration.main.size = (320,240)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
time.sleep(30)
while cpt < maxFrames:
    
    im = picam2.capture_array()
    im = cv2.flip(im, -1)
    im = cv2.rotate(im, cv2.ROTATE_180)

    filename = os.path.join(save_dir, f"Stop_{cpt}.jpg")
    print(f"saving image {filename}")
    success = cv2.imwrite(filename, im)
    if not success:
        print(f"Failed to save image {filename}")
    
    cv2.imshow("im", im)
    key = cv2.waitKey(1)
    if key == 27:  # ESC key to exit
        break
    
    time.sleep(0.5)
    cpt += 1

cv2.destroyAllWindows()
