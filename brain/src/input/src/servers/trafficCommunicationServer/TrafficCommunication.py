
# Import necessary modules
from twisted.internet import reactor
from udpStream import udpStream
from tcpServer import tcpServer
from locsys_SIM import LocsysGather
from Useful.dataDealer import dataDealer
from Useful.periodicTask_test import periodicTask
from Useful.locationDealer import locationDealer

class TrafficCommunication():
    def __init__(self, encrypt_key, streamPort=9000, commPort=5000):
        # Initialize data dealer and location dealer
        self.data_dealer = dataDealer()
        self.location_dealer = locationDealer()

        # Initialize LocsysGather with location dealer
        self.Locsys = LocsysGather(self.location_dealer)

        # Initialize tcpServer with data dealer and location dealer
        self.tcp_factory = tcpServer(self.data_dealer, self.location_dealer)

        # Initialize udpStream with streamPort, commPort, and encrypt_key
        self.udp_factory = udpStream(9000, commPort, encrypt_key)

        # Initialize periodicTask with data dealer
        self.period_task = periodicTask(0.1, self.data_dealer, self.location_dealer)

        # Initialize reactor
        self.reactor = reactor

        # Listen for TCP connections on commPort
        self.reactor.listenTCP(commPort, self.tcp_factory)

        # Listen for UDP connections on streamPort
        self.reactor.listenUDP(9001, self.udp_factory)

    def run(self):
        # Start periodic task
        self.period_task.start()

        # Run the reactor
        self.reactor.run()

    def stop(self):
        # Stop LocsysGather
        self.Locsys.stop()

        # Stop periodic task
        self.period_task.stop()


if __name__ == "__main__":
    # Specify the filename for the private key
    filename = "Useful/privatekey_server_test.pem"

    # Create an instance of TrafficCommunication
    traffic_communication = TrafficCommunication(filename)

    # Run the traffic communication
    traffic_communication.run()

    traffic_communication.stop()
