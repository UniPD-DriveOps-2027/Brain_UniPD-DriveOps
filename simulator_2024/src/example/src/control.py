#!/usr/bin/env python3
import json
from pynput import keyboard
import cv2 as cv
import names_and_constants as nac
from RcBrainThread import RcBrainThread
from std_msgs.msg import String
from sensor_msgs.msg import Image
from utils.msg import IMU
from cv_bridge import CvBridge
from time import time, sleep
import signal
import numpy as np
import os, sys

import rospy

class RemoteControlTransmitterProcess():
    # ===================================== INIT==========================================
    def __init__(self):
        """Run on the PC. It forwards the commans from the user via KeboardListenerThread to the RcBrainThread. 
        The RcBrainThread converts them into actual commands and sends them to the remote via a socket connection.
        
        """
        self.dirKeys   = ['w', 'a', 's', 'd']
        self.paramKeys = ['t','g','y','h','u','j','i','k', 'r', 'p']
        self.pidKeys = ['z','x','v','b','n','m']
        self.allKeys = self.dirKeys + self.paramKeys + self.pidKeys
        self.rcBrain   =  RcBrainThread()   
        # rospy.init_node('EXAMPLEnode', anonymous=False)     
        self.publisher = rospy.Publisher('/automobile/command', String, queue_size=1)

        #kewboard listener thread, non-blocking
        self.keyboardListenerThread = keyboard.Listener(on_press = self.keyPress, on_release = self.keyRelease)
        self.keyboardListenerThread.start()

    # ===================================== RUN ==========================================
    def run(self):
        """Apply initializing methods and start the threads. 
        """
        with keyboard.Listener(on_press = self.keyPress, on_release = self.keyRelease) as listener: 
            listener.join()
            cv.waitKey(1)
	
    # ===================================== KEY PRESS ====================================
    def keyPress(self,key):
        """Processing the key pressing 
        Parameters
        ----------
        key : pynput.keyboard.Key
            The key pressed
        """                                     
        try:
            if key.char == 'q':
                print('Exiting...')
                cv.destroyAllWindows()
                nod.keyboardListenerThread.stop()   
                raise KeyboardInterrupt
            if key.char == 'r':
                os.system('rosservice call /gazebo/reset_simulation')                             
            if key.char in self.allKeys:
                keyMsg = 'p.' + str(key.char)

                self._send_command(keyMsg)
    
        except: pass
        
    # ===================================== KEY RELEASE ==================================
    def keyRelease(self, key):
        """Processing the key realeasing.
        Parameters
        ----------
        key : pynput.keyboard.Key
            The key realeased. 
        """ 
        if key == keyboard.Key.esc:                        #exit key      
            self.publisher.publish('{"action":"3","steerAngle":0.0}')   
            return False
        try:                                               
            if key.char in self.allKeys:
                keyMsg = 'r.'+str(key.char)

                self._send_command(keyMsg)
    
        except: pass                                                              
                 
    # ===================================== SEND COMMAND =================================
    def _send_command(self, key):
        """Transmite the command to the remotecontrol receiver. 
        Parameters
        ----------
        inP : Pipe
            Input pipe. 
        """
        command = self.rcBrain.getMessage(key)
        if command is not None:
            command = json.dumps(command)
            self.publisher.publish(command)  

os.system('clear')
print('Manual Control starting...')

# stop the car with ctrl+c
def handler(signum, frame):
    print("Exiting ...")
    nod.keyboardListenerThread.stop()
    if nac.SIMULATOR_FLAG:
        os.system('rosservice call gazebo/pause_physics')
    cv.destroyAllWindows()
    sleep(.99)
    exit()


if __name__ == '__main__': 
    signal.signal(signal.SIGINT, handler)  
    try:
        rospy.init_node('manual_controller', anonymous=False)
        rospy.sleep(.1)  # wait for publisher to register to roscore
        nod = RemoteControlTransmitterProcess()

        while not rospy.is_shutdown():
            key = cv.waitKey(1)
            sleep(1/15)

    except KeyboardInterrupt:
        print("Shutting down")
        nod.keyboardListenerThread.stop()
        sleep(.5)
        cv.destroyAllWindows()
        exit(0)
    except rospy.ROSInterruptException:
        pass