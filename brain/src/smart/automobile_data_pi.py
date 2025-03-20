#!/usr/bin/python3
from automobile_data_interface import Automobile_Data
import helper_functions as hf
from std_msgs.msg import Float32, Bool, String
from utils.msg import IMU, localisation, vehicles
import rospy
import collections
import numpy as np

SONAR_THRESHOLD = 5

SONAR_DEQUE_LENGTH = 10

IMU_DEQUE_LENGTH = 10


CLASSIFY_DEQUE_LENGTH = 4

class AutomobileDataPi(Automobile_Data):
    def __init__(self,
                 trig_control=True,
                 trig_bno=False,
                 trig_enc=False,
                 trig_sonar=False,
                 trig_cam=False,
                 trig_gps=False,
                 trig_estimation=False,
                 trig_ESP32=False,
                 ) -> None:
        # initialize the parent class
        super().__init__()

        self.YAW_GLOBAL_OFFSET = -90  #to be changed before starting

        # ADDITIONAL VARIABLES
        self.right_sonar_distance_buffer = collections.deque(maxlen=SONAR_DEQUE_LENGTH)
        self.left_sonar_distance_buffer = collections.deque(maxlen=SONAR_DEQUE_LENGTH)

        self.center_sonar_distance = 3.0
        self.center_sonar_distance_buffer = collections.deque(maxlen=SONAR_DEQUE_LENGTH)
        self.filtered_center_sonar_distance = 3.0

        self.encoder_velocity_buffer = collections.deque(maxlen=SONAR_DEQUE_LENGTH)
        self.reachedPosition = False

        self.obstacle_buffer = collections.deque(maxlen=CLASSIFY_DEQUE_LENGTH)
        self.sign_buffer = collections.deque(maxlen=CLASSIFY_DEQUE_LENGTH)

        self.is_position_reliable = True
        self.estimation_last_encoder_distance = 0.0
        self.estimation_last_yaw_est = 0.0

        self.x_buffer = collections.deque(maxlen=5)
        self.y_buffer = collections.deque(maxlen=5)

        #IMU moving buffer
        self.yaw_buffer = collections.deque(maxlen=IMU_DEQUE_LENGTH)     


        # PUBLISHERS AND SUBSCRIBERS
        if trig_control:
            self.pub_speed     = rospy.Publisher('/automobile/command/speed', Float32, queue_size=1)
            self.pub_steer     = rospy.Publisher('/automobile/command/steer', Float32, queue_size=1)
            self.pub_stop      = rospy.Publisher('/automobile/command/stop', Float32, queue_size=1)
            self.pub_position  = rospy.Publisher('/automobile/command/position', Float32, queue_size=1)
            self.pub_closest_node = rospy.Publisher('/automobile/closest_node', Float32, queue_size=1)
            self.pub_next_event = rospy.Publisher('/automobile/next_event', String, queue_size=1)
            self.pub_current_state = rospy.Publisher('/automobile/current_state', String, queue_size=1)
            self.sub_position  = rospy.Subscriber("/automobile/feedback/position", Bool, self.feedback_position_callback)
        if trig_bno:
            self.sub_imu       = rospy.Subscriber('/automobile/imu', IMU, self.imu_callback)
        if trig_enc:
            self.sub_encSpeed  = rospy.Subscriber('/automobile/encoder/speed', Float32, self.encoder_velocity_callback)
            self.sub_encDist   = rospy.Subscriber('/automobile/encoder/distance', Float32, self.encoder_distance_callback)
            self.reset_rel_pose()
        if trig_sonar:
            self.sub_son_ahead_center = rospy.Subscriber('/automobile/sonar/center', Float32, self.center_sonar_callback)
            self.sub_right     = rospy.Subscriber('/automobile/sonar/right', Float32, self.right_sonar_callback)
            self.sub_left      = rospy.Subscriber('/automobile/sonar/left', Float32, self.left_sonar_callback)
        if trig_cam:
            raise NotImplementedError("cam not implemented yet")
        if trig_gps:
            self.sub_pos       = rospy.Subscriber("/automobile/vehicles", vehicles, self.position_callback)
        if trig_estimation:
            self.trig_estimation = trig_estimation
            print("ESTIMATION ENABLED")
        if trig_ESP32:
            self.sub_obstacle  = rospy.Subscriber("/automobile/obstacle", Float32, self.obstacle_callback)
            self.sub_sign      = rospy.Subscriber("/automobile/sign", Float32, self.sign_callback)

    def center_sonar_callback(self, data) -> None:
        """Receive and store distance of an obstacle ahead in
        :acts on: self.sonar_distance, self.filtered_sonar_distance
        """
        self.center_sonar_distance = data.data if data.data > 0 else self.center_sonar_distance
        self.center_sonar_distance_buffer.append(self.center_sonar_distance)
        self.filtered_center_sonar_distance = np.median(self.center_sonar_distance_buffer)
        print("-----------------------------------------")
        print(f"BUFFER: {self.center_sonar_distance_buffer}")
        print("-----------------------------------------")
        self.sonar_distance = self.center_sonar_distance
        self.filtered_sonar_distance = self.filtered_center_sonar_distance

    def right_sonar_callback(self, data) -> None:
        """Receive and store distance of an obstacle ahead in
        :acts on: self.sonar_distance, self.filtered_sonar_distance
        """
        self.right_sonar_distance = data.data if data.data > 0 else self.right_sonar_distance
        self.right_sonar_distance_buffer.append(self.right_sonar_distance)
        self.filtered_right_sonar_distance = np.median(self.right_sonar_distance_buffer)
    
    def left_sonar_callback(self, data) -> None:
        """Receive and store distance of an obstacle ahead in
        :acts on: self.sonar_distance, self.filtered_sonar_distance
        """
        self.left_sonar_distance = data.data if data.data > 0 else self.left_sonar_distance
        self.left_sonar_distance_buffer.append(self.left_sonar_distance)
        self.filtered_left_sonar_distance = np.median(self.left_sonar_distance_buffer)

    def position_callback(self, data) -> None:
        """Receive and store global coordinates from GPS
        :acts on: self.x, self.y
        """
        pL = np.array([data.posA, data.posB])
        pR = hf.mL2mR(pL)
        tmp_x = pR[0] - self.WB/2*np.cos(self.yaw)
        tmp_y = pR[1] - self.WB/2*np.sin(self.yaw)
        self.x_buffer.append(tmp_x)
        self.y_buffer.append(tmp_y)
        self.x = np.mean(self.x_buffer)
        self.y = np.mean(self.y_buffer)
        self.x_est = self.x
        self.y_est = self.y
        self.x_GPS = self.x
        self.y_GPS = self.y

    def imu_callback(self, data) -> None:
        """Receive and store rotation from IMU
        :acts on: self.roll, self.pitch, self.yaw, self.roll_deg,
                  self.pitch_deg, self.yaw_deg
        :acts on: self.accel_x, self.accel_y, self.accel_z, self.gyrox,
                  self.gyroy, self.gyroz
        """
        return
        if not self.STARTED_WITH_IMU:
            self.roll = np.deg2rad(data.roll)
            self.pitch = np.deg2rad(data.pitch)
            self.IMU_yaw = np.deg2rad(data.yaw) - np.deg2rad(self.YAW_GLOBAL_OFFSET)
            
            #self.yaw = hf.diff_angle(np.deg2rad(data.yaw) + self.yaw_offset, 0.0)
            #self.IMU_yaw = np.deg2rad(data.yaw) - np.deg2rad(self.YAW_GLOBAL_OFFSET)  #reading yaw and adjusting with global offset
            #self.IMU_yaw = (np.deg2rad(360) - self.IMU_yaw)%np.deg2rad(360)               #change from clockwise to counterclockwise
            # if (self.IMU_yaw < np.deg2rad(45)) or (self.IMU_yaw > np.deg2rad(315)):       #assign value multiple of pi/2 based on quadrant  
            #     self.IMU_yaw = 0.0
            # elif (self.IMU_yaw < np.deg2rad(135)) and (self.IMU_yaw > np.deg2rad(45)):
            #     self.IMU_yaw = np.deg2rad(90)
            # elif (self.IMU_yaw < np.deg2rad(225)) and (self.IMU_yaw > np.deg2rad(135)):
            #     self.IMU_yaw = np.deg2rad(180)
            # elif (self.IMU_yaw < np.deg2rad(315)) and (self.IMU_yaw > np.deg2rad(225)):
            #     self.IMU_yaw = np.deg2rad(270)

            self.roll_deg = np.rad2deg(self.roll)
            self.pitch_deg = np.rad2deg(self.pitch)
            self.yaw_deg = np.rad2deg(self.yaw)

            self.accel_x = data.accelx
            self.accel_y = data.accely
            self.accel_z = data.accelz

            self.gyrox = data.gyrox
            self.gyroy = data.gyroy
            self.gyroz = data.gyroz

    def encoder_distance_callback(self, data) -> None:
        """Callback when an encoder distance message is received
        :acts on: self.encoder_distance
        :needs to: call update_rel_position
        """
        self.encoder_distance = data.data
        self.update_rel_position()

    def encoder_velocity_callback(self, data) -> None:
        """Callback when an encoder velocity message is received
        :acts on: self.encoder_velocity
        """
        self.encoder_velocity = data.data
        self.encoder_velocity_buffer.append(self.encoder_velocity)
        self.filtered_encoder_velocity = np.median(self.encoder_velocity_buffer)
        
    def obstacle_callback(self, data) -> None:
        """Callback when an ESP32 detects an obstacle (in 2024 it only detects cars)
        :acts on: self.obstacle
        """
        self.obstacle = data.data
        self.obstacle_buffer.append(self.obstacle)
        self.filtered_obstacle = np.median(self.obstacle_buffer) 

        
    def sign_callback(self, data) -> None:
        """Callback when an ESP32 detects an sign (in 2024 it only detects cars)
        :acts on: self.sign
        """
        self.sign = data.data
        self.sign_buffer.append(self.sign)
        self.filtered_sign = np.median(self.sign_buffer)

    # COMMAND ACTIONS
    def drive_speed(self, speed=0.0) -> None:
        """Set the speed of the car
        :acts on: self.speed
        :param speed: speed of the car [m/s], defaults to 0.0
        """
        speed = Automobile_Data.normalizeSpeed(speed)   # normalize speed
        self.speed = speed #eugen, addded for the dashboard TODO change the name to be appropiate for dashboard application
        self.pub_speed.publish(speed)

    def drive_angle(self, angle=0.0) -> None:
        """Set the steering angle of the car
        :acts on: self.steer
        :param angle: [deg] desired angle, defaults to 0.0
        """
        angle = Automobile_Data.normalizeSteer(angle)   # normalize steer
        self.steer = angle
        self.pub_steer.publish(angle)

    def stop(self, angle=0.0) -> None:
        """Hard/Emergency stop the car
        :acts on: self.speed, self.steer
        :param angle: [deg] stop angle, defaults to 0.0
        """
        angle = Automobile_Data.normalizeSteer(angle)   # normalize steer
        self.steer = angle
        self.pub_stop.publish(angle)

    # ADDITIONAL METHODS
    def drive_distance(self, dist=0.0):
        self.reachedPosition = False
        self.pub_position.publish(dist)

    def feedback_position_callback(self, data):
        self.reachedPosition = data.data

    def publish_closest_node(self, data = 0.0):
        self.pub_closest_node.publish(data)
        
    def publish_next_event(self, data):
        self.pub_next_event.publish(data)

    def publish_current_state(self, data):
        self.pub_current_state.publish(data)