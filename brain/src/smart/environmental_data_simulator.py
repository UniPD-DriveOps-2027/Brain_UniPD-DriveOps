#!/usr/bin/python3
"""
environmental_data_pi.py — ROS2 Jazzy
Replaces environmental_data_simulator.py.
Subscriptions are created on the car node (already a rclpy Node).
"""
import numpy as np
import json
import names_and_constants as nac
import helper_functions as hf
from utils.msg import Semaphore

VEHICLE_CLOSE_RADIUS = 0.5  # [m]


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):   return int(obj)
        if isinstance(obj, np.floating):  return float(obj)
        if isinstance(obj, np.ndarray):   return obj.tolist()
        return super().default(obj)


class EnvironmentalData:
    def __init__(self,
                 car,               # AutomobileDataPi node — subscriptions go here
                 trig_v2v=False,
                 trig_v2x=False,
                 trig_semaphore=False) -> None:

        self._node = car

        # V2V
        self.other_vehicles = {}

        # V2X
        self.obstacle_list = []
        self.obstacle_map = {
            nac.STOP:                    1,
            nac.PRIORITY:                2,
            nac.PARK:                    3,
            nac.CROSSWALK:               4,
            nac.HW_ENTER:                5,
            nac.HW_EXIT:                 6,
            nac.ROUNDABOUT:              7,
            nac.ONE_WAY:                 8,
            nac.TRAFFIC_LIGHT:           9,
            nac.STATIC_CAR_ON_ROAD:      10,
            nac.STATIC_CAR_PARKING:      11,
            nac.PEDESTRIAN_ON_CROSSWALK: 12,
            nac.PEDESTRIAN_ON_ROAD:      13,
            nac.NO_SIGN:                 14,
        }
        self.sign_name_map = {
            'stop':                   nac.STOP,
            'priority':               nac.PRIORITY,
            'parking':                nac.PARK,
            'crosswalk':              nac.CROSSWALK,
            'highway_entry':          nac.HW_ENTER,
            'highway_end':            nac.HW_EXIT,
            'roundabout':             nac.ROUNDABOUT,
            'one_way':                nac.ONE_WAY,
            'traffic_light':          nac.TRAFFIC_LIGHT,
            'static_car_on_road':     nac.STATIC_CAR_ON_ROAD,
            'static_car_parking':     nac.STATIC_CAR_PARKING,
            'pedestrian_on_crosswalk':nac.PEDESTRIAN_ON_CROSSWALK,
            'pedestrian_on_road':     nac.PEDESTRIAN_ON_ROAD,
            'no_sign':                nac.NO_SIGN,
        }

        # SEMAPHORE
        self.semaphore_states = {
            nac.MASTER:     0,
            nac.SLAVE:      0,
            nac.ANTIMASTER: 0,
            nac.START:      0,
            nac.ANTISLAVE:  0,
        }
        self.semaphore_positions = {
            nac.MASTER:     np.array([0.0, 0.0]),
            nac.SLAVE:      np.array([0.0, 0.0]),
            nac.ANTIMASTER: np.array([0.0, 0.0]),
            nac.START:      np.array([0.0, 0.0]),
            nac.ANTISLAVE:  np.array([0.0, 0.0]),
        }

        # ── Subscribers (created on the car node) ──────────────────── #
        if trig_v2v:
            from utils.msg import Vehicles
            self._node.create_subscription(
                Vehicles, '/automobile/vehicles', self.v2v_callback, 1)

        if trig_v2x:
            from utils.msg import Environmental
            self._pub_v2x = self._node.create_publisher(
                Environmental, '/automobile/environment', 1)
        else:
            self._pub_v2x = None

        if trig_semaphore:
            self._node.create_subscription(
                Semaphore, '/automobile/semaphore/master',
                self.semaphore_master_callback, 1)
            self._node.create_subscription(
                Semaphore, '/automobile/semaphore/slave',
                self.semaphore_slave_callback, 1)
            self._node.create_subscription(
                Semaphore, '/automobile/semaphore/antimaster',
                self.semaphore_antimaster_callback, 1)
            self._node.create_subscription(
                Semaphore, '/automobile/semaphore/start',
                self.semaphore_start_callback, 1)
            self._node.create_subscription(
                Semaphore, '/automobile/semaphore/antislave',
                self.semaphore_antislave_callback, 1)

    # ── V2V ───────────────────────────────────────────────────────── #
    def v2v_callback(self, data) -> None:
        self.other_vehicles[data.ID] = np.array([data.pos_a, data.pos_b])

    def get_closest_moving_vehicle(self, car_x, car_y):
        if self.other_vehicles:
            ID, pos = min(self.other_vehicles.items(),
                          key=lambda x: np.linalg.norm(np.array([car_x, car_y]) - x[1]))
            return ID, pos
        print("No moving vehicles detected")
        return -1, np.array([car_x, car_y])

    def is_other_vehicle_close(self, car_x, car_y):
        ID, pos = self.get_closest_moving_vehicle(car_x, car_y)
        if ID < 0:
            return False
        return np.linalg.norm(np.array([car_x, car_y]) - pos) < VEHICLE_CLOSE_RADIUS

    # ── V2X ───────────────────────────────────────────────────────── #
    def publish_obstacle(self, type, x, y):
        type_const = self.sign_name_map.get(str(type).lower())
        if type_const is None:
            print(f"[WARNING] Unknown sign type: {type}")
            return
        if type_const not in self.obstacle_map:
            print(f"[WARNING] Sign constant {type_const} not in obstacle_map")
            return
        if self._pub_v2x is None:
            return

        from utils.msg import Environmental
        msg = Environmental()
        msg.obstacle_id = self.obstacle_map[type_const]
        pL = hf.mR2mL(np.array([x, y]))
        msg.x = float(pL[0])
        msg.y = float(pL[1])
        self._pub_v2x.publish(msg)
        self.obstacle_list.append(f'{type} at ({x:.2f},{y:.2f}) m')

    # ── SEMAPHORE ─────────────────────────────────────────────────── #
    def semaphore_master_callback(self, data):
        self.semaphore_states[nac.MASTER]    = data.state
        self.semaphore_positions[nac.MASTER] = np.array([data.pos_x, data.pos_y])

    def semaphore_slave_callback(self, data):
        self.semaphore_states[nac.SLAVE]    = data.state
        self.semaphore_positions[nac.SLAVE] = np.array([data.pos_x, data.pos_y])

    def semaphore_antimaster_callback(self, data):
        self.semaphore_states[nac.ANTIMASTER]    = data.state
        self.semaphore_positions[nac.ANTIMASTER] = np.array([data.pos_x, data.pos_y])

    def semaphore_start_callback(self, data):
        self.semaphore_states[nac.START]    = data.state
        self.semaphore_positions[nac.START] = np.array([data.pos_x, data.pos_y])

    def semaphore_antislave_callback(self, data):
        self.semaphore_states[nac.ANTISLAVE]    = data.state
        self.semaphore_positions[nac.ANTISLAVE] = np.array([data.pos_x, data.pos_y])

    def get_semaphore_state(self, semaphore_key):
        assert semaphore_key in self.semaphore_states, f"Semaphore key not recognized: {semaphore_key}"
        return self.semaphore_states[semaphore_key]

    def get_closest_semaphore_state(self, car_position):
        closest = min(self.semaphore_positions.items(),
                      key=lambda x: np.linalg.norm(car_position - x[1]))
        print(f'Closest semaphore: {closest[0]}, state: {self.get_semaphore_state(closest[0])}')
        return closest[0], self.get_semaphore_state(closest[0])

    def __str__(self):
        return json.dumps({
            'other_vehicles': self.other_vehicles,
            'obstacle_list':  self.obstacle_list,
            'semaphore_states': self.semaphore_states,
        }, indent=2, cls=NumpyEncoder)