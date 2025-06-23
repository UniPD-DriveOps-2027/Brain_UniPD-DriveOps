#!/usr/bin/env python3

if __name__ == "__main__":
    import sys, os
    assert os.path.isfile("/catkin_ws/src/input/server/publickey_server.pem"), 'before'
    sys.path.append("/catkin_ws/src/input")
    assert os.path.isfile("/catkin_ws/src/input/server/publickey_server.pem"), 'after'
    # Import necessary modules
    from multiprocessing import Pipe
    from src.data.TrafficCommunication.useful.sharedMem import sharedMem
    from src.templates.workerprocess import WorkerProcess
    from src.data.TrafficCommunication.threads.threadTrafficCommunicaiton import (
        threadTrafficCommunication,
    )

class processTrafficCommunication(WorkerProcess):
    """This process receives the location of the car and sends it to the processGateway.
    
    Args:
        queueList (dictionary of multiprocessing.queues.Queue): Dictionary of queues where the ID is the type of messages.
        logging (logging object): Used for debugging.
        deviceID (int): The ID of the device.
        frequency (float): The frequency of communication.
    """

    # ====================================== INIT ==========================================
    def __init__(self, queueList, logging, deviceID, debugging, frequency=1):
        self.queuesList = queueList
        self.logging = logging
        self.shared_memory = sharedMem()
        self.filename = "src/data/TrafficCommunication/useful/publickey_server_test.pem"
        self.deviceID = deviceID
        self.frequency = frequency
        self.debugging = debugging
        super(processTrafficCommunication, self).__init__(self.queuesList)

    # ===================================== STOP ==========================================
    def stop(self):
        """Function for stopping threads and the process."""
        
        for thread in self.threads:
            thread.stop()
            thread.join()
        super(processTrafficCommunication, self).stop()

    # ===================================== RUN ==========================================
    def run(self):
        """Apply the initializing methods and start the threads."""

        super(processTrafficCommunication, self).run()
        rospy.init_node('traffic_communication_node', anonymous=True)  # Initialize ROS node

    # ===================================== INIT TH ======================================
    def _init_threads(self):
        """Create the Traffic Communication thread and add it to the list of threads."""

        TrafficComTh = threadTrafficCommunication(
            self.shared_memory, self.queuesList, self.deviceID, self.frequency, self.filename
        )
        self.threads.append(TrafficComTh)


# =================================== EXAMPLE =========================================
#             ++    THIS WILL RUN ONLY IF YOU RUN THE CODE FROM HERE  ++
#                  in terminal:    python3 processTrafficCommunication.py

if __name__ == "__main__":
    from multiprocessing import Queue
    import time
    import signal
    import subprocess
    import sys
    import rospy
    from std_msgs.msg import Float64
    from utils.msg import vehicles, environmental, localisation, IMU
    import queue

    def kill_process_on_port(port):
        try:
            cmd = f"sudo lsof -t -i:{port} | xargs --no-run-if-empty sudo kill -9"
            subprocess.check_call(cmd, shell=True)
            print(f"Processes using port {port} have been killed (if any).")
        except subprocess.CalledProcessError:
            print(f"No process is using port {port}.")



    shared_memory = sharedMem()
    locsysReceivePipe, locsysSendPipe = Pipe(duplex=False)
    queueList = {
        "Critical": Queue(),
        "Warning": Queue(),
        "General": Queue(),
        "Config": Queue(),
    }
    filename = "/catkin_ws/src/input/server/publickey_server.pem"
    #filename = "useful/publickey_server_test.pem"
    deviceID = 7
    frequency = 0.4
    traffic_communication = threadTrafficCommunication(
        shared_memory, queueList, deviceID, frequency, filename
    )
    traffic_communication.start()    

    # =================================== ROS =========================================
    rospy.init_node('serverNODE', anonymous=False)
    veh = vehicles()
    loc = localisation()
    # =============================== PUBLISHERS ======================================
    Vehicles_publisher = rospy.Publisher("/automobile/vehicles", vehicles, queue_size=1)
    Environment_publisher = rospy.Publisher("/automobile/environment", environmental, queue_size=1)
    # ============================== SUBSCRIPTIONS  ===================================

    # ROS Subscribers Setup

    def environment_callback(msg):
        #print(f"Received Obstacle ID: {msg.obstacle_id}, X: {msg.x}, Y: {msg.y}")
        msg_sign = {
            "reqORinfo": "info",
            "type": "historyData",
            "value1": msg.x,
            "value2": msg.y,
            "value3": msg.obstacle_id,
        }
        traffic_communication.tcp_factory.send_data_to_server(msg_sign)

    def car_position_callback(msg):
        #print(f"car_position_callback: X: {msg.x}, Y: {msg.y}")
        msg_position = {
            "reqORinfo": "info",
            "type": "devicePos",
            "value1": msg.x,
            "value2": msg.y,
        }
        traffic_communication.tcp_factory.send_data_to_server(msg_position)

    def car_speed_callback(msg):
        #print(f"car_speed_callback: Speed: {msg.data}")
        msg_speed = {
            "reqORinfo": "info",
            "type": "deviceSpeed",
            "value1": msg.data,
        }
        traffic_communication.tcp_factory.send_data_to_server(msg_speed)

    def car_yaw_callback(msg):
        #print(f"car_yaw_callback: Yaw: {msg.yaw}")
        msg_yaw = {
            "reqORinfo": "info",
            "type": "deviceRot",
            "value1": float(msg.yaw),
        }
        traffic_communication.tcp_factory.send_data_to_server(msg_yaw)

    # ROS Subscribers

    rospy.Subscriber('/automobile/environment', environmental, environment_callback)
    rospy.Subscriber('/automobile/localisation', localisation, car_position_callback)
    rospy.Subscriber('/automobile/speed', Float64, car_speed_callback)
    rospy.Subscriber('/automobile/imu', IMU, car_yaw_callback)

    try:
        while not rospy.is_shutdown():
            try:
                data = queueList["General"].get()
                veh.posA = float(data['msgValue']['x'] / 1000)
                veh.posB = float(data['msgValue']['y'] / 1000)
                print(f'X = {veh.posA} Y = {veh.posB}')
                Vehicles_publisher.publish(veh)

                #env_msg = environmental()
                #env_msg.obstacle_id = 1
                #env_msg.x = veh.posA + 0.001
                #env_msg.y = veh.posB + 0.001
                #Environment_publisher.publish(env_msg)

                # comment since the position send back in is automobile_data_pi.py
                #msg_position = {
                #    "reqORinfo": "info",
                #    "type": "devicePos",
                #    "value1": float(data['msgValue']['x']),
                #    "value2": float(data['msgValue']['y']),
                #}
                #traffic_communication.tcp_factory.send_data_to_server(msg_position)
                
            except queue.Empty:
                pass  # no data — just continue, and check is_shutdown again

    except (rospy.ROSInterruptException, KeyboardInterrupt):
        print("Shutting down safely hopefully")
    finally:
        print("Cleaning up...")
        traffic_communication.stop()
        kill_process_on_port(9000)
