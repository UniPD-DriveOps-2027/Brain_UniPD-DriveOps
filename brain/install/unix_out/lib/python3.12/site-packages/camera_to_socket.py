# #!/usr/bin/env python3
# """
# camera_to_socket.py
# Reads /oak/rgb/image_raw and forwards raw BGR frames
# to the dashboard over a Unix socket.
# """
# import socket, time, threading
# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge

# SOCKET_PATH = "/tmp/bfmc_camera_dashboard.sock"
# FRAME_W     = 320
# FRAME_H     = 240


# class CameraToSocket(Node):
#     def __init__(self):
#         super().__init__('camera_to_socket_node')
#         self._bridge = CvBridge()
#         self._conn   = None
#         self._lock   = threading.Lock()

#         # connect to the dashboard socket server in background
#         threading.Thread(target=self._connect_loop, daemon=True).start()

#         self.create_subscription(
#             Image, '/oak/rgb/image_raw', self._image_cb, 1)
#         self.get_logger().info("camera_to_socket started")

#     def _connect_loop(self):
#         while rclpy.ok():
#             try:
#                 s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#                 s.connect(SOCKET_PATH)
#                 self.get_logger().info("Connected to dashboard camera socket")
#                 with self._lock:
#                     self._conn = s
#                 # stay here until connection drops
#                 while rclpy.ok():
#                     time.sleep(1)
#                     try:
#                         s.send(b'')  # probe
#                     except:
#                         break
#             except Exception as e:
#                 self.get_logger().warn(f"Camera socket not ready: {e}")
#                 time.sleep(2)
#             with self._lock:
#                 self._conn = None

#     def _image_cb(self, msg: Image):
#         with self._lock:
#             if self._conn is None:
#                 return
#         try:
#             import cv2

#             frame = self._bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

#             # resize (keep if you want fixed dashboard size)
#             if frame.shape[:2] != (FRAME_H, FRAME_W):
#                 frame = cv2.resize(frame, (FRAME_W, FRAME_H))

#             # JPEG encode (THIS IS THE KEY CHANGE)
#             _, encoded = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])

#             data = encoded.tobytes()

#             with self._lock:
#                 if self._conn:
#                     # send size first (so receiver knows boundary)
#                     size = len(data).to_bytes(4, byteorder="little")
#                     print("sending frame bytes:", len(data))
#                     self._conn.sendall(size + data)
#         except Exception as e:
#             self.get_logger().warn(f"Camera send error: {e}")
#             with self._lock:
#                 self._conn = None


# def main(args=None):
#     rclpy.init(args=args)
#     node = CameraToSocket()
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         node.destroy_node()
#         rclpy.shutdown()


# if __name__ == '__main__':
#     main()
#!/usr/bin/env python3
"""
camera_to_socket.py
Reads /oak/rgb/image_raw and forwards raw BGR frames
to the dashboard over a Unix socket.
"""
import socket, time, threading
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

SOCKET_PATH = "/tmp/bfmc_camera_dashboard.sock"
FRAME_W     = 320
FRAME_H     = 240


class CameraToSocket(Node):
    def __init__(self):
        super().__init__('camera_to_socket_node')
        self._bridge = CvBridge()
        self._conn   = None
        self._lock   = threading.Lock()

        # connect to the dashboard socket server in background
        threading.Thread(target=self._connect_loop, daemon=True).start()

        self.create_subscription(
            Image, '/oak/rgb/image_raw', self._image_cb, 1)
        self.get_logger().info("camera_to_socket started")

    def _connect_loop(self):
        while rclpy.ok():
            try:
                s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                s.connect(SOCKET_PATH)
                self.get_logger().info("Connected to dashboard camera socket")
                with self._lock:
                    self._conn = s
                # stay here until connection drops
                while rclpy.ok():
                    time.sleep(1)
                    try:
                        s.send(b'')  # probe
                    except:
                        break
            except Exception as e:
                self.get_logger().warn(f"Camera socket not ready: {e}")
                time.sleep(2)
            with self._lock:
                self._conn = None

    def _image_cb(self, msg: Image):
        with self._lock:
            if self._conn is None:
                return
        try:
            frame = self._bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            import cv2
            if frame.shape[1] != FRAME_W or frame.shape[0] != FRAME_H:
                frame = cv2.resize(frame, (FRAME_W, FRAME_H))
            with self._lock:
                if self._conn:
                    self._conn.sendall(frame.tobytes())
        except Exception as e:
            self.get_logger().warn(f"Camera send error: {e}")
            with self._lock:
                self._conn = None


def main(args=None):
    rclpy.init(args=args)
    node = CameraToSocket()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()