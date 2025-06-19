#!/usr/bin/env python3
import socket
import os
import numpy as np
import cv2
import time
import signal
from ultralytics import YOLO
from unix_socket_camera import UnixSocketCamera

if __name__ == "__main__":
    cap = UnixSocketCamera(socket_addr="/tmp/bfmc_camera_brain.sock", frame_size=(320, 240))
    SIGN_CLASSIFIER_YOLO_PATH = "models/sign_classifier_yolo.tflite"
    # YOLO sign classifier
    sign_yolo = YOLO(SIGN_CLASSIFIER_YOLO_PATH, task='detect')
    names = sign_yolo.names
    
    frame_count = 0
    
    try:
        while cap.running:  # Use the running flag as condition
            success, frame = cap.read()
            if success:
                frame_count += 1
                print(f"[DEBUG] Processing frame {frame_count}")  # Debug output
                
                TL = (240, 10)   # x1, y1
                BR = (320, 70)   # x2, y2

                img = frame.copy()
                original_frame = img.copy()
                roi_frame = img[TL[1]:BR[1], TL[0]:BR[0]]  # Better variable name

                # Check if ROI is valid before processing
                if roi_frame.size > 0:
                    results = sign_yolo.track(roi_frame, persist=True, imgsz=256)

                    if results[0].boxes.id is not None:
                        ids = results[0].boxes.id.cpu().numpy().astype(int)
                        boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
                        class_ids = results[0].boxes.cls.int().cpu().tolist()

                        for track_id, box, class_id in zip(ids, boxes, class_ids):
                            x1, y1, x2, y2 = box
                            cx = (x1 + x2) // 2
                            cy = (y1 + y2) // 2
                            label = names[class_id]

                            cv2.rectangle(roi_frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
                            cv2.putText(roi_frame, f"{label}", (x1+10, y1 + 50),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 0, 255), 1)

                # Draw ROI rectangle on original frame for visualization
                cv2.rectangle(original_frame, TL, BR, (0, 255, 0), 2)
                cv2.putText(original_frame, "ROI", (TL[0], TL[1]-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

                # Display frames
                if roi_frame.size > 0:
                    cv2.imshow("FRAME", roi_frame)
                cv2.imshow("ORIGINAL", original_frame)
            else:
                # Add small delay when no frame is available
                time.sleep(0.01)
                
            # CRITICAL: This line is essential for OpenCV window updates
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # Press 'q' or ESC to quit
                print("[INFO] Quit key pressed")
                break

    except KeyboardInterrupt:
        print("Keyboard interrupt received...")
    finally:
        cap.shutdown()
        cv2.destroyAllWindows()
        print("Clean shutdown completed")