

import json
import time
from src.utils.messages.allMessages import Location
from src.utils.messages.messageHandlerSender import messageHandlerSender
from twisted.internet import protocol
import numpy as np

# The server itself. Creates a new Protocol for each new connection and has the info for all of them.
class tcpClient(protocol.ClientFactory):
    def __init__(self, connectionBrokenCllbck, locsysID, locsysFrequency, queue):
        self.connectiondata = None
        self.connection = None
        self.retry_delay = 1
        self.connectionBrokenCllbck = connectionBrokenCllbck
        self.locsysID = locsysID
        self.locsysFrequency = locsysFrequency
        self.queue = queue
        self.sendLocation = messageHandlerSender(self.queue, Location)

    def clientConnectionLost(self, connector, reason):
        print(
            "Connection lost with server ",
            self.connectiondata,
        )
        try:
            self.connectiondata = None
            self.connection = None
            self.connectionBrokenCllbck()
        except:
            pass

    def clientConnectionFailed(self, connector, reason):
        print(
            "Connection failed. Retrying in",
            self.retry_delay,
            "seconds... Possible server down or incorrect IP:port match",
        )
        time.sleep(self.retry_delay)
        connector.connect()

    def buildProtocol(self, addr):
        conn = SingleConnection()
        conn.factory = self
        return conn

    def send_data_to_server(self, message):
        if self.connection:
            self.connection.send_data(message)
            print("sending")
        else:
            print("No TCP connection to server.. We ccannot send message yet")

    def send_sign_to_server(self, value1, value2, value3):
        self.connection.send_historyData(self, value1, value2, value3)


# One class is generated for each new connection
class SingleConnection(protocol.Protocol):
    def connectionMade(self):
        peer = self.transport.getPeer()
        self.factory.connectiondata = peer.host + ":" + str(peer.port)
        self.factory.connection = self
        self.subscribeToLocaitonData(self.factory.locsysID, self.factory.locsysFrequency)
        print("Connection with server established : ", self.factory.connectiondata)

    def dataReceived(self, data):
        dat = data.decode()
        tmp_data = dat.replace("}{","}}{{")
        if tmp_data != dat:
            tmp_dat = tmp_data.split("}{")
            dat = tmp_dat[-1]
        da = json.loads(dat)

        if da["type"] == "location":
            da["id"] = self.factory.locsysID
            # fixed infinite loop on hooks (hopefully)
            self.factory.sendLocation.send(da)
        else:
            print(
                "got message from trafficcommunication server: ",
                self.factory.connectiondata,
            )
    def send_data(self, message):
        msg = json.dumps(message)
        #print("***")
        #print(msg)
        #print("***")
        self.transport.write(msg.encode())
    
    def subscribeToLocaitonData(self, id, frequency):
        # Sends the id you wish to subscribe to and the frequency you want to receive data. Frequency must be between 0.1 and 5. 
        print("*** subscribeToLocaitonData ***")
        msg = {
            "reqORinfo": "info",
            "type": "locIDsub",
            "locID": id,
            "freq": frequency,
        }
        self.send_data(msg)
    
    def send_historyData(self, value1, value2, value3):
        print("*** send_historyData ***")
        msg = {
            "reqORinfo": "info",
            "type": "historyData",
            "value1": value1, #pos x
            "value2": value2, #pos y                           
            "value3": value3, #obstacle id
        }
        self.send_data(msg)
    
    def unSubscribeToLocaitonData(self, id, frequency):
        # Unsubscribes from locaiton data. 
        msg = {
            "reqORinfo": "info",
            "type": "locIDubsub",
        }
        self.send_data(msg)
