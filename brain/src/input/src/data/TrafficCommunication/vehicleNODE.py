import rospy
from std_msgs.msg import Float64
from utils.msg import vehicles

if __name__ == "__main__":
    import sys

    sys.path.insert(0, "../../..")
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
        logging (logging object): Made for debugging.
    """

    def __init__(self, queueList, logging, deviceID):
        self.queuesList = queueList
        self.logging = logging
        self.shared_memory = sharedMem()
        self.filename = "src/data/TrafficCommunication/useful/publickey_server_test.pem"
        self.deviceID = deviceID
        super(processTrafficCommunication, self).__init__(self.queuesList)

    def stop(self):
        """Function for stopping threads and the process."""
        for thread in self.threads:
            thread.stop()
            thread.join()
        super(processTrafficCommunication, self).stop()

    def run(self):
        """Apply the initializing methods and start the threads."""
        super(processTrafficCommunication, self).run()
        rospy.init_node('traffic_communication_node', anonymous=True)  # Initialize ROS node

    def _init_threads(self):
        """Create the Traffic Communication thread and add to the list of threads."""
        TrafficComTh = threadTrafficCommunication(
            self.shared_memory, self.queuesList, self.deviceID, self.filename
        )
        self.threads.append(TrafficComTh)

if __name__ == "__main__":
    from multiprocessing import Queue, Event

    # Initialize ROS node
    #rospy.init_node('traffic_communication_node', anonymous=True)
    rospy.init_node('vehicletovehicleNODE', anonymous=False)

    # Create shared memory object
    shared_memory = sharedMem()

    # Create queues
    queueList = {
        "Critical": Queue(),
        "Warning": Queue(),
        "General": Queue(),
        "Config": Queue(),
    }

    # Define filename and deviceID
    filename = "useful/publickey_server_test.pem"
    deviceID = 1

    # Start Traffic Communication thread
    traffic_communication = threadTrafficCommunication(
        shared_memory, queueList, deviceID, filename
    )
    traffic_communication.start()

    try:
        # Create publishers for x and y topics
        #x_publisher = rospy.Publisher("/vehicle/x", Float64, queue_size=10)
        #y_publisher = rospy.Publisher("/vehicle/y", Float64, queue_size=10)
        Vehicles_publisher = rospy.Publisher("/automobile/vehicles", vehicles, queue_size=1)
        veh = vehicles()

        while not rospy.is_shutdown():
            # Get data from General queue
            data = queueList["General"].get()
            veh.posA  = float(data['msgValue']['x'])  # Convert to float
            veh.posB  = float(data['msgValue']['Y'])  # Convert to float

            
            #x = data['msgValue']['x']
            #y = data['msgValue']['Y']
            
            print(f'X = {veh.posA } Y = {veh.posB}')
            Vehicles_publisher.publish(veh)

            #x_publisher.publish(Float64(x))
            #y_publisher.publish(Float64(y))

    except rospy.ROSInterruptException:
        pass

    finally:
        traffic_communication.stop() 
