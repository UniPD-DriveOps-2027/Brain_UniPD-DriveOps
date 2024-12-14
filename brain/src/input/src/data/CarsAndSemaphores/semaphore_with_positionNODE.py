#!/usr/bin/env python3

import rospy
from utils.msg import semaphore

# if __name__ == "__main__":
import sys

sys.path.insert(0, "../../..")

from src.templates.workerprocess import WorkerProcess
from src.data.CarsAndSemaphores.threads.threadCarsAndSemaphores import (
    threadCarsAndSemaphores,
)


class processCarsAndSemaphores(WorkerProcess):
    """This process will receive the location of the other cars and the location and the state of the semaphores.

    Args:
        queueList (dictionary of multiprocessing.queues.Queue): Dictionary of queues where the ID is the type of messages.
        logging (logging object): Made for debugging.
    """

    # ====================================== INIT ==========================================
    def __init__(self, queueList, logging=False):
        self.queuesList = queueList
        self.logging = logging
        super(processCarsAndSemaphores, self).__init__(self.queuesList)

    # ===================================== STOP ==========================================
    def stop(self):
        """Function for stopping threads and the process."""
        for thread in self.threads:
            thread.stop()
            thread.join()
        super(processCarsAndSemaphores, self).stop()

    # ===================================== RUN ==========================================
    def run(self):
        """Apply the initializing methods and start the threads."""
        super(processCarsAndSemaphores, self).run()

    # ===================================== INIT TH ======================================
    def _init_threads(self):
        """Create the thread and add to the list of threads."""
        CarsSemTh = threadCarsAndSemaphores(self.queuesList)
        self.threads.append(CarsSemTh)


# =================================== EXAMPLE =========================================
#             ++    THIS WILL RUN ONLY IF YOU RUN THE CODE FROM HERE  ++
#                  in terminal:    python3 processCarsAndSemaphores.py
"""
if __name__ == "__main__":
    from multiprocessing import Queue
    import time

    queueList = {
        "Critical": Queue(),
        "Warning": Queue(),
        "General": Queue(),
        "Config": Queue(),
    }

    allProcesses = list()
    process = processCarsAndSemaphores(queueList)
    process.start()

    time.sleep(3)
    print(queueList["General"].get())

    process.stop()
"""
if __name__ == "__main__":
    from multiprocessing import Queue
    import time

    queueList = {
        "Critical": Queue(),
        "Warning": Queue(),
        "General": Queue(),
        "Config": Queue(),
    }

    allProcesses = list()
    process = processCarsAndSemaphores(queueList)
    process.start()

    rospy.init_node('semaphoreNODE', anonymous=False)

    try:
        Semaphoremaster_publisher = rospy.Publisher("/automobile/semaphore/master", semaphore, queue_size=1)
        Semaphoreslave_publisher = rospy.Publisher("/automobile/semaphore/slave", semaphore, queue_size=1)
        Semaphoreantimaster_publisher = rospy.Publisher("/automobile/semaphore/antimaster", semaphore, queue_size=1)
        Semaphoreantislave_publisher = rospy.Publisher("/automobile/semaphore/antislave", semaphore, queue_size=1)
        Semaphorestart_publisher = rospy.Publisher("/automobile/semaphore/start", semaphore, queue_size=1)
        sem = semaphore()

        while not rospy.is_shutdown():
            if not queueList["General"].empty():
                message = queueList["General"].get()
                msg_value = message["msgValue"]
                ID = int(msg_value["id"])
                #print(message)
                
                if "state" in msg_value:
                    if msg_value["state"] == 'green':
                        sem.state = 2
                    elif msg_value["state"] == 'yellow':
                        sem.state = 1
                    elif msg_value["state"] == 'red':
                        sem.state = 0
                    else:
                        sem.state = -1  # Default state if "state" key has an unexpected value

                if sem.state != -1:
                    sem.pos_x = float(msg_value["x"])
                    sem.pos_y = float(msg_value["y"])
                    if ID == 2:
                        Semaphoremaster_publisher.publish(sem)
                    elif ID == 4:
                        Semaphoreslave_publisher.publish(sem)
                    elif ID == 3:
                        Semaphoreantimaster_publisher.publish(sem)
                    elif ID == 1:
                        Semaphorestart_publisher.publish(sem)
                    elif ID == 5:
                        Semaphoreantislave_publisher.publish(sem)

    except rospy.ROSInterruptException:
        pass
    
    finally:
        process.terminate()
