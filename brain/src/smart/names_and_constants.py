#!/usr/bin/python3

# file to import in the other files

###############################################################################
###############################################################################
###############################################################################
###############################################################################


# This is handled with the argparse in main_brain
RANDOM_START = None
SPEED_CHALLENGE = None
RC_MODE = None
SIMULATOR_FLAG = None
SHOW_IMGS = None
RESUME = None
NORTH = None
SOUTH = None
EAST = None
WEST = None

<<<<<<< Updated upstream
=======
# names_and_constants.py
TESTING = False

# Configurazioni eventi
EVENT_CONFIGS = {
    # Highway to tunnel
    "hw_tunnel": {
        "starting_coords": [0.39, 12.2],
        "checkpoints": [999, 143]
    },
    "tunnel": {
        "starting_coords": [2.42, 10.62],
        "checkpoints": [999, 143]
    },
    "round1": {
        "starting_coords": [17.3, 6.0],
        "checkpoints": [999, 397, 200]
    },

    "round2": {
        "starting_coords": [17.96, 8.81],
        "checkpoints": [999, 333, 200]
    },
    "round3": {
        "starting_coords": [17.96, 8.81],
        "checkpoints": [999, 200]
    },
    "round4": {
        "starting_coords": [17.96, 8.81],
        "checkpoints": [999,377,490]
    },
    # South entrance of the roundabout to no lane
    "no_lane_right": {
        "starting_coords": [17.96, 8.81],
        "checkpoints": [999, 328, 150]
    },
    # East entrance of the roundabout to no lane
    "no_lane_left": {
        "starting_coords": [19.28, 11.83],
        "checkpoints": [999, 333, 150]
    },
    "no_lane_highway": {
        "starting_coords": [16.02, 11.42],
        "checkpoints": [999, 335, 210]
    },
    "no_lane_cuza": {
        "starting_coords": [17.32, 7.04],
        "checkpoints": [999, 333, 210]
    },
    # North entrance of the roundabout to Highway
    "highway": {
        "starting_coords": [17, 11.73],
        "checkpoints": [999, 170]
    },
    "crosswalk": {
        "starting_coords": [13.02,  4.41],
        "checkpoints": [999, 145]
    },
    "parking": {
        "starting_coords": [7.73, 0.75], #[4.41, 0.75]  [6.07, 0.75]  [7.73, 0.75]
        "checkpoints": [450, 411]
    },
    "bus": {
        "starting_coords": [16.42, 4.48],
        "checkpoints": [999, 125]
    },
    "test": {
        "starting_coords": [0.39, 6.14],
        "checkpoints": [999, 131, 114, 434]
    },
    "test2": {
        "starting_coords": [12.02, 0.75],    #  1.41,3.91
        "checkpoints": [460, 466, 420, 396, 306, 319, 260, 197, 207, 150, 123, 118, 91, 451, 455, 444, 30, 130, 147, 175, 121, 92, 95, 107, 109, 97, 163, 190, 236, 373, 382, 407, 334, 352, 502]
    },
    "intersection_straight": {
        "starting_coords": [0.92, 13.17],   
        "checkpoints": [999, 119]
    },
    "intersection_left": {
        "starting_coords": [0.37, 9.84],   
        "checkpoints": [999, 145, 153]
    },
    "intersection_right": {
        "starting_coords": [0.84, 5.26],   
        "checkpoints": [999, 145, 153]
    }
    #"intersection_straight": {
    #    "starting_coords": [15.54, 3.41],   
    #    "checkpoints": [999, 445, 500]
    #}
#94, 95, 121, 92, 107, 109, 130, 147, 175, 123, 118, 91, 451, 455, 466, 420, 396, 306, 319, 260, 197, 207, 150, 97, 163, 190, 236, 373, 382, 407, 444, 30, 334, 352, 502
}


>>>>>>> Stashed changes
EVENT_SETTINGS = None  # Variable to store the event settings

# BRAIN
# ========================= STATES ==========================
START_STATE = 'start_state'
END_STATE = 'end_state'
DOING_NOTHING = 'doing_nothing'
LANE_FOLLOWING = 'lane_following'
APPROACHING_STOPLINE = 'approaching_stopline'
INTERSECTION_NAVIGATION = 'intersection_navigation'
TURNING_RIGHT = 'turning_right'
TURNING_LEFT = 'turning_left'
GOING_STRAIGHT = 'going_straight'
TRACKING_LOCAL_PATH = 'tracking_local_path'
ROUNDABOUT_NAVIGATION = 'roundabout_navigation'
WAITING_FOR_PEDESTRIAN = 'waiting_for_pedestrian'
WAITING_FOR_GREEN = 'waiting_for_green'
WAITING_AT_STOPLINE = 'waiting_at_stopline'
OVERTAKING_STATIC_CAR = 'overtaking_static_car'
OVERTAKING_MOVING_CAR = 'overtaking_moving_car'
TAILING_CAR = 'tailing_car'
AVOIDING_ROADBLOCK = 'avoiding_roadblock'
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

EVENT_TYPES = [INTERSECTION_STOP_EVENT,             #0
               INTERSECTION_TRAFFIC_LIGHT_EVENT,    #1
               INTERSECTION_PRIORITY_EVENT,         #2
               JUNCTION_EVENT,                      #3
               ROUNDABOUT_EVENT,                    #4
               CROSSWALK_EVENT,                     #5
               PARKING_EVENT,                       #6
               HIGHWAY_EXIT_EVENT,                  #7
               HIGHWAY_ENTRANCE_EVENT]              #8


# ======================== ACHIEVEMENTS ========================
# consider adding all the tasks, may be too cumbersome
PARK_ACHIEVED = 'park_achieved'
NO_LANE_ACHIEVED = 'no_lane_achieved'

# ======================== CONDITIONS ==========================
CAN_OVERTAKE = 'can_overtake'
HIGHWAY = 'highway'
TRUST_GPS = 'trust_gps'
CAR_ON_PATH = 'car_on_path'
REROUTING = 'rerouting'
BUMPY_ROAD = 'bumpy_road'
NO_LANE = 'no_lane'


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
ROADBLOCK = 'roadblock'

# ENVIROMENTAL SERVER
STATIC_CAR_ON_ROAD = 'static_car_on_road'
STATIC_CAR_PARKING = 'static_car_parking'
PEDESTRIAN_ON_CROSSWALK = 'pedestrian_on_crosswalk'
PEDESTRIAN_ON_ROAD = 'pedestrian_on_road'
ROADBLOCK = 'roadblock'
BUMPY_ROAD = 'bumpy_road'

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
