import cv2
import numpy as np
import time
from unix_socket_camera import UnixSocketCamera

import json
with open('data/events_config.json', 'r') as file:
    events_config = json.load(file)

cap = UnixSocketCamera(socket_addr="/tmp/bfmc_camera_brain.sock", frame_size=(320, 240))

try:
    while True:
        ret, frame = cap.read()

        # Resize the frame to match the preview resolution (faster display)
        frame_resized = frame

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame_resized, cv2.COLOR_RGB2HSV)

        # Define the range of pink in HSV (Hue range for pink: 140-170)
        lower_pink = np.array([140, 100, 100])  # Lower bound for pink
        upper_pink = np.array([170, 255, 255])  # Upper bound for pink

        # Create a mask for pink regions
        mask = cv2.inRange(hsv, lower_pink, upper_pink)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find the largest contour, assuming the pink object is the largest object
            largest_contour = max(contours, key=cv2.contourArea)

            # Get the moments to find the centroid
            moments = cv2.moments(largest_contour)
            if moments["m00"] != 0:
                cx = int(moments["m10"] / moments["m00"])
                cy = int(moments["m01"] / moments["m00"])

                # Draw a red dot at the centroid (Red is BGR: (0, 0, 255))
                cv2.circle(frame_resized, (cx, cy), 10, (0, 0, 255), -1)  # Red in BGR

        # Display the resulting frame (now resized for faster performance)
        cv2.imshow("Camera", frame_resized)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Stopping camera...")
    picam2.stop()

cv2.destroyAllWindows()