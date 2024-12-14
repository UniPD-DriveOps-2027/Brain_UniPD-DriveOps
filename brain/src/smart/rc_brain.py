#!/usr/bin/python3
import cv2 as cv
import pygame
from time import time, sleep
import numpy as np

import names_and_constants as nac
from automobile_data_interface import Automobile_Data
from controller3 import Controller
from detection import Detection
from parkman import Maneuvers

JOYSTICK_DEADZONE = 0.1
TRIGGER_DEADZONE = 0.1

OBSTACLE_CONTROL_DISTANCE = 0.5
OBSTACLE_STOP_DISTANCE = 0.2

IDLE_TIME = 120

class RC_Brain:
    def __init__(self, 
                 car: Automobile_Data,
                 controller: Controller,
                 detection: Detection, 
                 max_speed=0.3):
        
        print("Initialize rc_brain")
        self.car = car
        self.controller = controller
        self.detect = detection
        self.max_speed = max_speed

        self.car.drive(speed=0.0, angle=0.0)
        
        self.rc_speed = 0.0
        self.rc_angle = 0.0
        self.park = Maneuvers()
        self.car_pov = False
        self.lane_following = False

        print("Initialize Joystick")
        pygame.init()
        self.joysticks = {}
        self.joystick = None
        self.event = pygame.event
        done = False
        while not done:
            print("Trying to connect to a Joystick ...")
            for event in self.event.get():
                if event.type == pygame.JOYDEVICEADDED:
                    # This event will be generated when the program starts for every
                    # joystick, filling up the list without needing to create them manually.
                    joy = pygame.joystick.Joystick(event.device_index)
                    self.joysticks[joy.get_instance_id()] = joy
                    print(f"Joystick {joy.get_instance_id()} connencted")
                    self.joystick = next(iter(self.joysticks.values()))
                    done = True
            print("\033c")
        sleep(0.1)

        print('RC_Brain initialized')
        self.last_input_time = time()
    
    def run(self):        
        if self.joysticks.values():
            print('JOYSTICK CONNECTED')
            print('============================================================')
            print(f' SPEED:          {100*self.rc_speed:.0f} cm/s')
            print(f' STEER:          {self.rc_angle:.0f} deg')
            print('============================================================')
            print('PARAMETERS: ')
            print(f' MAX_SPEED:      {100*self.max_speed:.0f} cm/s')
            print('============================================================')
            print('COMMANDS: ')
            print(' Left Joystick  : Steer')
            print(' Right Trigger  : Forward Speed')
            print(' Left  Trigger  : Reverse Speed')
            print(' A              : Follow Lane')
            print(' B + Left/Right : Park Maneuver')
            print(' Y              : Car_POV')
            print(' D-Pad Up/Down  : Increase/Decrease MAX_SPEED')
            print(' X              : Stop and Kill Car')
            print('============================================================')

        else:
            print('NO JOYSTICK CONNECTED')
        
        self.rc_inputs()

        if self.car_pov:
            self.show_cam()

        if self.lane_following:
            self.follow_lane()
            self.last_input_time = time()
            print('LANE FOLLOWING')
            print('Press A to stop')
        
        if not nac.SIMULATOR_FLAG:
            self.control_for_obstacles()

        self.car.drive(speed=self.rc_speed, angle=self.rc_angle)

        self.check_idle(self.last_input_time)
        
    def rc_inputs(self):
        for event in pygame.event.get():
            self.last_input_time = time()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 3: # 'X' button on XBOX controller
                    print("X button pressed: Exiting ...")
                    self.car.stop()
                    sleep(1)
                    print("\033c")
                    exit()

                if event.button == 4: # 'Y' button on XBOX controller
                    print("Y button pressed: Car_POV ...")
                    self.car_pov = not self.car_pov
                    if not self.car_pov:
                        cv.destroyAllWindows()
                    sleep(0.1)
                
                if event.button == 0: # 'A' button on XBOX controller
                    print("A button pressed: Following Lane...")
                    hat1 = self.joystick.get_hat(0)
                    self.lane_following = not self.lane_following
                
                if event.button == 1: # 'B' button on XBOX controller
                    hat1 = self.joystick.get_hat(0)
                    pad_horizontal_value = hat1[0]
                    if pad_horizontal_value == 1:
                        print("\033c")
                        print("B button pressed: Parking Right ...")
                        self.park.parallel_parking(self.car, nac.RIGHT_PARK)
                    elif pad_horizontal_value == -1:
                        print("\033c")
                        print("B button pressed: Parking Left ...")
                        self.park.parallel_parking(self.car, nac.LEFT_PARK)
            
            # Cancel LANE_FOLLOWING if use joystick
            if event.type == pygame.JOYAXISMOTION:
                if abs(event.value) > JOYSTICK_DEADZONE:
                    self.lane_following = False
            
            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                self.joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")
                self.joystick = next(iter(self.joysticks.values()))

            if event.type == pygame.JOYDEVICEREMOVED:
                del self.joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")
                self.car.stop()
                sleep(0.1)
            
        if not self.lane_following:
            # STEER CONTROL
            # Axis 0 = Left Joystick -- Horizontal
            # Range = [-1,1]
            left_joy_value = self.joystick.get_axis(0)
            if abs(left_joy_value) > JOYSTICK_DEADZONE:
                # self.rc_angle = left_joy_value * self.car.MAX_STEER                                      # linear behaviour
                self.rc_angle = (np.sign(left_joy_value) * np.abs(left_joy_value)**2) * self.car.MAX_STEER # non-linear behaviour
            else:
                self.rc_angle = 0.0

            # SPEED CONTROL
            # Axis 4 = Right Trigger
            # Range = [-1,1]
            right_trig_value = self.joystick.get_axis(4)
            right_trig_value = (right_trig_value + 1)/2
            # REVERSE SPEED CONTROL
            # Axis 5 = Left Trigger
            # Range = [-1,1]
            left_trig_value = self.joystick.get_axis(5)
            left_trig_value = (left_trig_value + 1)/2
            if abs(right_trig_value) > TRIGGER_DEADZONE:
                self.rc_speed = right_trig_value * self.max_speed
            elif abs(left_trig_value) > TRIGGER_DEADZONE:
                self.rc_speed = left_trig_value * self.car.MIN_SPEED
            else:
                self.rc_speed = 0.0
            # self.car.drive(speed=self.rc_speed, angle=self.rc_angle)

        # MAX_SPEED ADJUST
        # Hat 0 [1] = Up and Down on D-Pad
        # Values = (-1, 0, 1)
        hat = self.joystick.get_hat(0)
        pad_vertical_value = hat[1]
        if pad_vertical_value:
            self.max_speed += pad_vertical_value*0.05
            if self.max_speed < self.car.MIN_SPEED:
                self.max_speed = self.car.MIN_SPEED
            elif self.max_speed > self.car.MAX_SPEED:
                self.max_speed = self.car.MAX_SPEED
            sleep(0.15)

    def show_cam(self):
        img = self.car.frame.copy()
        cv.imshow('Car_POV', img)
        if cv.waitKey(1) == 27:
            cv.destroyAllWindows()

    def follow_lane(self):
        e2, e3,_ = self.detect.detect_lane(self.car.frame, False)
        _, angle_ref = self.controller.get_control(e2, e3, 0, self.max_speed, no_lane=False)
        self.rc_angle = np.rad2deg(angle_ref)
        self.rc_speed = self.max_speed
        # self.car.drive(speed=self.rc_speed, angle=self.rc_angle)

    def control_for_obstacles(self):
        # check for obstacles
        dist = self.car.filtered_sonar_distance
        if dist < OBSTACLE_CONTROL_DISTANCE:
            self.lane_following = False
            if dist < OBSTACLE_STOP_DISTANCE and self.rc_speed > 0:
                self.rc_speed = 0.0
            # self.car.drive_speed(speed=0.0)

    def check_idle(self, time):
        if (time()-time) > IDLE_TIME:
            print("\033c")
            print("Idle Time Exceeded. Exiting ...")
            self.car.stop()
            sleep(1)
            exit()