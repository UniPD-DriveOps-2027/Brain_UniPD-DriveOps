#!/usr/bin/env python3
"""
serialNODE — ROS2 Jazzy version
Forwards commands from /automobile/command to the serial port,
and re-publishes responses to per-command topics on demand.

Service: command_feedback_en (utils/srv/Subscribing)
"""

import json
import serial
import threading

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from utils.srv import Subscribing  # was: subscribing, subscribingResponse

from filehandler      import FileHandler
from messageconverter import MessageConverter


class SerialNode(Node):
    def __init__(self):
        super().__init__('serialNODE')

        dev_file = '/dev/ttyACM0'
        log_file = 'historyFile.txt'

        self._serial = serial.Serial(dev_file, 19200, timeout=0.1)
        self._serial.flushInput()
        self._serial.flushOutput()

        self._history       = FileHandler(log_file)
        self._converter     = MessageConverter()
        self._buff          = ""
        self._is_response   = False
        self._subscribers   = {}           # code → list[Publisher]
        self._sub_lock      = threading.Lock()

        self.create_subscription(String, '/automobile/command', self._write_cb, 10)
        self.create_service(Subscribing, 'command_feedback_en', self._subscribe_cb)

        # Read serial in a daemon thread
        self._thread = threading.Thread(target=self._read_loop, daemon=True)
        self._thread.start()
        self.get_logger().info("serialNODE started")

    # ------------------------------------------------------------------ #
    #  Serial read loop
    # ------------------------------------------------------------------ #
    def _read_loop(self):
        while rclpy.ok():
            ch = self._serial.read()
            try:
                ch = ch.decode('ascii')
            except UnicodeDecodeError:
                continue

            if ch == '@':
                self._is_response = True
                if self._buff:
                    self._dispatch(self._buff)
                self._buff = ""
            elif ch == '\r':
                self._is_response = False
                if self._buff:
                    self._dispatch(self._buff)
                self._buff = ""

            if self._is_response:
                self._buff += ch
            self._history.write(ch)

    def _dispatch(self, response: str):
        key = response[1:5]
        with self._sub_lock:
            pubs = self._subscribers.get(key, [])
        for pub in pubs:
            pub.publish(String(data=response))

    # ------------------------------------------------------------------ #
    #  Write callback
    # ------------------------------------------------------------------ #
    def _write_cb(self, msg: String):
        command     = json.loads(msg.data)
        command_msg = self._converter.get_command(**command)
        self._serial.write(command_msg.encode('ascii'))
        self._history.write(command_msg)

    # ------------------------------------------------------------------ #
    #  Subscribe service
    # ------------------------------------------------------------------ #
    def _subscribe_cb(self, request: Subscribing.Request,
                           response: Subscribing.Response) -> Subscribing.Response:
        with self._sub_lock:
            if request.subscribing:
                if request.code in self._subscribers:
                    for pub in self._subscribers[request.code]:
                        if pub.topic == request.topic:
                            response.topic = False
                            return response
                    pub = self.create_publisher(String, request.topic, 1)
                    self._subscribers[request.code].append(pub)
                else:
                    pub = self.create_publisher(String, request.topic, 1)
                    self._subscribers[request.code] = [pub]
                response.topic = True
            else:
                if request.code in self._subscribers:
                    for pub in list(self._subscribers[request.code]):
                        if pub.topic == request.topic:
                            self.destroy_publisher(pub)
                            self._subscribers[request.code].remove(pub)
                            response.topic = True
                            return response
                response.topic = False
        return response

    def destroy_node(self):
        self._serial.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SerialNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
