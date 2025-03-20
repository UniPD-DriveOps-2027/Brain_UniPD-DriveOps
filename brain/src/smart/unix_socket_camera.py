#!/usr/bin/env python3
import socket
import os
import numpy as np
import cv2

class UnixSocketCamera:
    def __init__(self, socket_addr="/tmp/bfmc_socket.sock", frame_size=(320, 240)):
        self.socket_addr = socket_addr
        self.frame_size = frame_size
        self.msg_size = frame_size[0] * frame_size[1] * 3  # Total size for an RGB888 frame
        self.sock = None
        self.data = b''

        # Set up the socket (create or connect)
        self.setup_socket()

    def setup_socket(self):
        # Remove the socket if it already exists (server-style setup)
        if os.path.exists(self.socket_addr):
            os.remove(self.socket_addr)

        # Create and bind the Unix socket
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            self.sock.bind(self.socket_addr)
            self.sock.listen(1)  # Act like a server and wait for a connection
            print(f"Socket created and waiting for a client at {self.socket_addr}")
            
            # Accept a connection
            self.conn, _ = self.sock.accept()
            print("Client connected.")
        except socket.error as e:
            print(f"Error setting up socket: {e}")
            self.sock = None

    def read(self):
        if not self.conn:
            print("No active connection.")
            return False, None

        try:
            # Ensure we have enough data for a full frame
            while len(self.data) < self.msg_size:
                packet = self.conn.recv(10000)#4096  8192
                if not packet:
                    raise ConnectionError("Client disconnected.")
                self.data += packet

            # Extract frame and keep remaining data
            frame_data = self.data[:self.msg_size]
            self.data = self.data[self.msg_size:]
            frame = np.frombuffer(frame_data, dtype=np.uint8).reshape(
                self.frame_size[1], self.frame_size[0], 3
            )
            return True, frame
        except (ConnectionError, socket.error) as e:
            print(f"Socket error: {e}")
            self.conn.close()
            self.conn = None
            return False, None

    def release(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")
        if self.sock:
            self.sock.close()
            print("Socket closed.")

if __name__ == "__main__":
    cap = UnixSocketCamera(socket_addr="/tmp/bfmc_socket.sock", frame_size=(320, 240)) #320, 240 or 1152, 648
    
    try:
        while True:
            success, frame = cap.read()
            if success:
                cv2.imshow("Unix Socket Camera", frame)
                #crop_img = frame[100:, 80:240]
                #cv2.imshow("Street", crop_img)
                #cv2.imshow("Signs", frame[:, 200:])
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("Waiting for a new frame...")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        cap.release()
        cv2.destroyAllWindows()

