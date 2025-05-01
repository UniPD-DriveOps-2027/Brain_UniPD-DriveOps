import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImageOverlayNode:
    def __init__(self):
        rospy.init_node('image_overlay_node', anonymous=True)
        self.subscriber = rospy.Subscriber('/automobile/image_raw', Image, self.image_callback)
        self.bridge = CvBridge()
        self.overlay_image = cv2.imread('overlay.png', cv2.IMREAD_UNCHANGED)
        self.overlay_image = cv2.resize(self.overlay_image, (320, 240))
    
    def image_callback(self, msg):
        # Convert ROS image to OpenCV format
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        if self.overlay_image.shape[2] == 4:
            # Extract alpha channel and create a mask
            overlay_rgb = self.overlay_image[:, :, :3]
            alpha_mask = self.overlay_image[:, :, 3] / 255.0
            
            # Blend images with transparency
            for c in range(3):
                frame[:, :, c] = (frame[:, :, c] * (1 - 0.5 * alpha_mask) + 
                                  overlay_rgb[:, :, c] * (0.5 * alpha_mask))
        else:
            # If no alpha channel, just do a simple overlay with 50% opacity
            frame = cv2.addWeighted(frame, 0.5, self.overlay_image, 0.5, 0)
        
        # Show the result
        cv2.imshow('Overlay Image', frame)
        cv2.waitKey(1)


def main():
    node = ImageOverlayNode()
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

