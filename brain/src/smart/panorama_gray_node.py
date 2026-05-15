#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from message_filters import Subscriber, ApproximateTimeSynchronizer

import cv2
import numpy as np


def _imgmsg_to_mono8(msg: Image) -> np.ndarray:
    return np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width).copy()


def _make_mono8_imgmsg(frame: np.ndarray, stamp=None, frame_id: str = '') -> Image:
    msg = Image()
    msg.height   = frame.shape[0]
    msg.width    = frame.shape[1]
    msg.encoding = 'mono8'
    msg.step     = frame.shape[1]
    msg.data     = frame.tobytes()
    if stamp is not None:
        msg.header.stamp = stamp
    msg.header.frame_id = frame_id
    return msg


def horizontal_image_stitching(images, crop_percent=0.05):
    left_img  = images[0]
    right_img = images[1]

    h1, w1 = left_img.shape[:2]
    h2, w2 = right_img.shape[:2]

    target_height = min(h1, h2)
    left_img  = cv2.resize(left_img,  (int(w1 * target_height / h1), target_height))
    right_img = cv2.resize(right_img, (int(w2 * target_height / h2), target_height))

    if crop_percent > 0:
        _, w1 = left_img.shape[:2]
        _, w2 = right_img.shape[:2]
        left_img  = left_img[:,  int(w1 * crop_percent):]
        right_img = right_img[:, :w2 - int(w2 * crop_percent)]

    # Stitcher exposure compensator requires CV_8UC3
    left_bgr  = cv2.cvtColor(left_img,  cv2.COLOR_GRAY2BGR)
    right_bgr = cv2.cvtColor(right_img, cv2.COLOR_GRAY2BGR)

    stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
    status, panorama_bgr = stitcher.stitch([left_bgr, right_bgr])

    if status != cv2.Stitcher_OK:
        panorama_bgr = np.hstack((left_bgr, right_bgr))

    return cv2.cvtColor(panorama_bgr, cv2.COLOR_BGR2GRAY)


class PanoramaGrayNode(Node):
    def __init__(self):
        super().__init__('panorama_gray_node')

        self.left_sub  = Subscriber(self, Image, '/oak/left/image_raw')
        self.right_sub = Subscriber(self, Image, '/oak/right/image_raw')

        self.sync = ApproximateTimeSynchronizer(
            [self.left_sub, self.right_sub],
            queue_size=10,
            slop=0.1,
        )
        self.sync.registerCallback(self.image_callback)

        self.pub = self.create_publisher(Image, '/oak/panorama_gray/image_raw', 10)

        self.get_logger().info('Panorama grayscale node started.')

    def image_callback(self, left_msg, right_msg):
        try:
            left_img  = _imgmsg_to_mono8(left_msg)
            right_img = _imgmsg_to_mono8(right_msg)

            panorama = horizontal_image_stitching([left_img, right_img], crop_percent=0.05)

            self.pub.publish(_make_mono8_imgmsg(
                panorama,
                stamp=self.get_clock().now().to_msg(),
                frame_id='oak_panorama_gray_frame',
            ))

        except Exception as e:
            self.get_logger().error(f'Panorama stitching failed: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = PanoramaGrayNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
