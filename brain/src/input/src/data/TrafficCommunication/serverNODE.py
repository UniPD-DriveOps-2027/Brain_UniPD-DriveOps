
import rospy
from std_msgs.msg import Float64
from utils.msg import vehicles, environmental

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../../..")

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

    shared_memory = sharedMem()
    locsysReceivePipe, locsysSendPipe = Pipe(duplex=False)
    queueList = {
        "Critical": Queue(),
        "Warning": Queue(),
        "General": Queue(),
        "Config": Queue(),
    }
    filename = "useful/publickey_server.pem"
    #filename = "useful/publickey_server_test.pem"
    deviceID = 3
    frequency = 0.4
    traffic_communication = threadTrafficCommunication(
        shared_memory, queueList, deviceID, frequency, filename
    )
    traffic_communication.start()    

    # =================================== ROS =========================================
    rospy.init_node('serverNODE', anonymous=False)
    # =============================== PUBLISHERS ======================================
    Vehicles_publisher = rospy.Publisher("/automobile/vehicles", vehicles, queue_size=1)
    Environment_publisher = rospy.Publisher("/automobile/environment", environmental, queue_size=1)
    # ============================== SUBSCRIPTIONS  ===================================

    def environment_callback(msg):
        print(f"Received Obstacle ID: {msg.obstacle_id}, X: {msg.x}, Y: {msg.y}")
        msg_sign = {
            "reqORinfo": "info",
            "type": "historyData",
            "value1": msg.x,             # pos x
            "value2": msg.y,             # pos y
            "value3": msg.obstacle_id,   # obstacle id
        }
        traffic_communication.tcp_factory.send_data_to_server(msg_sign)


    rospy.Subscriber('/automobile/environment', environmental, environment_callback)
    veh = vehicles()
    try:
        while not rospy.is_shutdown():
            data = queueList["General"].get()
            veh.posA  = float(data['msgValue']['x'])
            veh.posB  = float(data['msgValue']['y'])
            print(f'X = {veh.posA} Y = {veh.posB}')
            Vehicles_publisher.publish(veh)

            # Example environment message
            env_msg = environmental()
            env_msg.obstacle_id = 1
            env_msg.x = veh.posA + 0.001
            env_msg.y = veh.posB + 0.001
            Environment_publisher.publish(env_msg)

    except rospy.ROSInterruptException:
        pass
    finally:
        traffic_communication.stop()
