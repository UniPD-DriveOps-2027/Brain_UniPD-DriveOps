#!/usr/bin/python3

# file to import in the other files

###############################################################################
###############################################################################
###############################################################################
###############################################################################


# This is handled with the argparse in main_brain
RANDOM_START = None
RC_MODE = None
SIMULATOR_FLAG = None
SHOW_IMGS = None

NORTH = None
SOUTH = None
EAST = None
WEST = None

# names_and_constants.py
TESTING = False

# Configurazioni eventi
EVENT_CONFIGS = {
    "tunnel": {
        "starting_coords": [13.11, 1.98],
        "checkpoints": [9999, 422, 398, 303, 260, 87, 118, 410, 406, 445, 164, 237, 333, 374, 30, 85, 148, 177, 143, 135, 98, 55, 30, 98, 111, 121, 92, 130]
    },
    "round": {
        "starting_coords": [15.38, 11,42],
        "checkpoints": [455, 350]
    },
    "highway": {
        "starting_coords": [16.65, 11.74],
        "checkpoints": [50, 149]
    },
    "crosswalk": {
        "starting_coords": [15.75,  4.36],
        "checkpoints": [50, 148]
    },
    "parking": {
        "starting_coords": [7.67, 0.75],
        "checkpoints": [50, 412,389]
    },
     "test": {
        "starting_coords": [7.67, 0.75],
        "checkpoints": [50, 410]
    }

}


EVENT_SETTINGS = None  # Variable to store the event settings

# BRAIN
# ========================= STATES ==========================
START_STATE = 'start_state'
END_STATE = 'end_state'
LANE_FOLLOWING = 'lane_following'
APPROACHING_STOPLINE = 'approaching_stopline'
TURNING_RIGHT = 'turning_right'
TURNING_LEFT = 'turning_left'
TRACKING_LOCAL_PATH = 'tracking_local_path'
WAITING_FOR_PEDESTRIAN = 'waiting_for_pedestrian'
WAITING_FOR_GREEN = 'waiting_for_green'
WAITING_AT_STOPLINE = 'waiting_at_stopline'
OVERTAKING_STATIC_CAR = 'overtaking_static_car'
OVERTAKING_MOVING_CAR = 'overtaking_moving_car'
TAILING_CAR = 'tailing_car'
PARKING = 'parking'
CROSSWALK_NAVIGATION = 'crosswalk_navigation'
CLASSIFYING_OBSTACLE = 'classifying_obstacle'

# ======================== ROUTINES ==========================
FOLLOW_LANE = 'follow_lane'
DETECT_STOPLINE = 'detect_stopline'
SLOW_DOWN = 'slow_down'
ACCELERATE = 'accelerate'
CONTROL_FOR_SIGNS = 'control_for_signs'
CONTROL_FOR_OBSTACLES = 'control_for_obstacles'
CONTROL_FOR_PEDESTRIAN = 'control_for_pedestrian'
UPDATE_STATE = 'update_state'
DRIVE_DESIRED_SPEED = 'drive_desired_speed'

# ========================== EVENTS ==========================
INTERSECTION_STOP_EVENT = 'intersection_stop_event'
INTERSECTION_TRAFFIC_LIGHT_EVENT = 'intersection_traffic_light_event'
INTERSECTION_PRIORITY_EVENT = 'intersection_priority_event'
JUNCTION_EVENT = 'junction_event'
ROUNDABOUT_EVENT = 'roundabout_event'
CROSSWALK_EVENT = 'crosswalk_event'
PARKING_EVENT = 'parking_event'
END_EVENT = 'end_event'
HIGHWAY_EXIT_EVENT = 'highway_exit_event'
HIGHWAY_ENTRANCE_EVENT = 'highway_entrance_event'
TUNNEL_EVENT = 'tunnel_event'

EVENT_TYPES = [INTERSECTION_STOP_EVENT,             #0
               INTERSECTION_TRAFFIC_LIGHT_EVENT,    #1
               INTERSECTION_PRIORITY_EVENT,         #2
               JUNCTION_EVENT,                      #3
               ROUNDABOUT_EVENT,                    #4
               CROSSWALK_EVENT,                     #5
               PARKING_EVENT,                       #6
               HIGHWAY_EXIT_EVENT,                  #7
               HIGHWAY_ENTRANCE_EVENT,              #8
               TUNNEL_EVENT                         #9 
               ]                             


# ======================== ACHIEVEMENTS ========================
# consider adding all the tasks, may be too cumbersome
PARK_ACHIEVED = 'park_achieved'
NO_LANE_ACHIEVED = 'no_lane_achieved'

# ======================== CONDITIONS ==========================
CAN_OVERTAKE = 'can_overtake'
HIGHWAY = 'highway'
CAR_ON_PATH = 'car_on_path'
REROUTING = 'rerouting'
BUMPY_ROAD = 'bumpy_road'
NO_LANE = 'no_lane'
TUNNEL = 'tunnel'

###############################################################################
###############################################################################
###############################################################################
###############################################################################


# DETECTION
# PARKING SIGNS
PARK = 'park'
CLOSED_ROAD = 'closed_road'
HW_EXIT = 'hw_exit'
HW_ENTER = 'hw_enter'
STOP = 'stop'
ROUNDABOUT = 'roundabout'
PRIORITY = 'priority'
CROSSWALK = 'cross_walk'
ONE_WAY = 'one_way'
NO_SIGN = 'NO_sign'
TRAFFIC_LIGHT = 'traffic_light'
SIGN_NAMES = [PARK,
              CLOSED_ROAD,
              HW_EXIT,
              HW_ENTER,
              STOP,
              ROUNDABOUT,
              PRIORITY,
              CROSSWALK,
              ONE_WAY,
              NO_SIGN]

# obstacles
CAR = 'car'
PEDESTRIAN = 'pedestrian'

# ENVIROMENTAL SERVER
STATIC_CAR_ON_ROAD = 'static_car_on_road'
STATIC_CAR_PARKING = 'static_car_parking'
PEDESTRIAN_ON_CROSSWALK = 'pedestrian_on_crosswalk'
PEDESTRIAN_ON_ROAD = 'pedestrian_on_road'


# sempahores
MASTER = 'master'
SLAVE = 'slave'
ANTIMASTER = 'antimaster'
START = 'start'
ANTISLAVE = 'antislave'

# semaphore states
GREEN = 2
YELLOW = 1
RED = 0

###############################################################################
###############################################################################
###############################################################################
###############################################################################

# AUTOMOBILE DATA

# PARKING SUBSTATES
LOCALIZING_PARKING_SPOT = 1
CHECKING_FOR_PARKED_CARS = 2
STEP0 = 69
T_STEP2 = 4
T_STEP3 = 5
T_STEP4 = 6
T_STEP5 = 7
S_STEP2 = 9
S_STEP3 = 10
S_STEP4 = 11
S_STEP5 = 12
S_STEP6 = 13
S_STEP7 = 14
PARK_END = 16
# park types
T_PARK = 't'
S_PARK = 's'
# parking side
RIGHT_PARK = 'right'
LEFT_PARK = 'left'
TH = None
