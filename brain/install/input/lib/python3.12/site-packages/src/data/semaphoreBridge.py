#!/usr/bin/env python3
"""
semaphoreBridge.py
Starts the unmodified Bosch semaphore engine (threadSemaphores / udpListener),
drains its output queue and publishes to the correct ROS2 topics that
environmental_data_simulator.py expects.

Topics published:
  /automobile/semaphore/master      (utils/Semaphore)
  /automobile/semaphore/slave       (utils/Semaphore)
  /automobile/semaphore/antimaster  (utils/Semaphore)
  /automobile/semaphore/start       (utils/Semaphore)
  /automobile/semaphore/antislave   (utils/Semaphore)
  /automobile/vehicles              (utils/Vehicles)   ← other cars on track

Semaphore ID → role mapping:
  Edit SEMAPHORE_ID_MAP below to match whatever IDs the server assigns.
  Check the competition documentation / udpStreamSIM output to confirm.
"""

import threading
import logging
from multiprocessing import Queue

import rclpy
from rclpy.node import Node

from utils.msg import Semaphore, Vehicles

# ── Engine imports (Bosch code, untouched) ────────────────────────────── #
from data.Semaphores.threads.threadSemaphores import threadSemaphores

# ── Semaphore ID → ROS2 topic suffix ─────────────────────────────────── #
# Keys are the integer IDs the server broadcasts. Adjust if needed.
SEMAPHORE_ID_MAP = {
    0: 'start',
    1: 'master',
    2: 'slave',
    3: 'antimaster',
    4: 'antislave',
}

STATE_MAP = {
    'red':    0,
    'yellow': 1,
    'green':  2,
}

# Both cars and semaphores are sent via the Semaphores sender (msgID=2).
# Distinguish them by the presence of the 'state' key in the payload.
MSG_ID_SEMAPHORES = 2


class SemaphoreBridge(Node):

    def __init__(self, queue_list: dict):
        super().__init__('semaphore_bridge')
        self._queue_list = queue_list

        # ── Publishers ───────────────────────────────────────────────── #
        self._sem_pubs = {
            role: self.create_publisher(Semaphore, f'/automobile/semaphore/{role}', 1)
            for role in SEMAPHORE_ID_MAP.values()
        }
        self._vehicles_pub = self.create_publisher(Vehicles, '/automobile/vehicles', 1)

        # ── Drain thread ─────────────────────────────────────────────── #
        self._running = True
        self._drain_thread = threading.Thread(target=self._drain, daemon=True)
        self._drain_thread.start()

    def _drain(self):
        general_q: Queue = self._queue_list['General']
        while self._running and rclpy.ok():
            try:
                msg = general_q.get(timeout=1.0)
            except Exception:
                continue

            msg_id    = msg.get('msgID')
            msg_value = msg.get('msgValue', {})

            if msg_id == MSG_ID_SEMAPHORES:
                if 'state' in msg_value:
                    self._publish_semaphore(msg_value)
                else:
                    self._publish_vehicle(msg_value)

    def _publish_semaphore(self, value: dict):
        sem_id = value.get('id')
        role   = SEMAPHORE_ID_MAP.get(sem_id)
        if role is None:
            self.get_logger().warn(f'Unknown semaphore id: {sem_id}')
            return

        state_raw = value.get('state', 'red')
        state_int = STATE_MAP.get(str(state_raw).lower(), 0)

        ros_msg         = Semaphore()
        ros_msg.state   = state_int
        ros_msg.pos_x   = float(value.get('x', 0.0))
        ros_msg.pos_y   = float(value.get('y', 0.0))
        self._sem_pubs[role].publish(ros_msg)

    def _publish_vehicle(self, value: dict):
        ros_msg        = Vehicles()
        ros_msg.id     = int(value.get('id', 0))
        ros_msg.pos_a  = float(value.get('x', 0.0))
        ros_msg.pos_b  = float(value.get('y', 0.0))
        self._vehicles_pub.publish(ros_msg)

    def destroy_node(self):
        self._running = False
        super().destroy_node()


def main(args=None):
    queue_list = {
        'Critical': Queue(),
        'Warning':  Queue(),
        'General':  Queue(),
        'Config':   Queue(),
    }

    logger = logging.getLogger('semaphoreBridge')

    # Start the unmodified Bosch engine thread
    engine = threadSemaphores(queue_list, logger, debugging=False)
    engine.start()

    rclpy.init(args=args)
    node = SemaphoreBridge(queue_list)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        engine.stop()
        engine.join()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
