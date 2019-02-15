from scapy.all import *
from packets.packet import Packet
from bitstring import BitArray# flip bit of string


class ScapyPacket(Packet):

    def __init__(self, headerSize):
        self.headerSize = headerSize

        #sizes in bytes
        '''
            self.ETHERNET_HEADER_SIZE = 14
            self.IP_HEADER_SIZE = 20
            self.UDP_HEADER_SIZE = 8
            self.HEADER_SIZE = self.ETHERNET_HEADER_SIZE + \
                self.IP_HEADER_SIZE + self.UDP_HEADER_SIZE


            self.payloadSize = len(payload)
            self.checksumSize = 4
            '''
        self.IP_DST_ADDRESS = "127.0.0.1"
        self.UDP_PORT = 12349

        self.frameBase=IP(dst=self.IP_DST_ADDRESS) / UDP(sport=self.UDP_PORT)

    def send(self):
        """send loaded packet"""
        self.sendString(self.payload)
        return self.totalSize

    def sendString(self, string):
        sendp(self.frameBase / Raw(string), verbose=0)

    def sendErroned(self):
        erronedPayload= self.getFlipedPayload(0)
        return self.send()

    def setPayload(self, payload):
        self.payloadSize = len(payload)
        self.computeTotalSize()
        self.payload = payload.encode('utf-8')

        #print (str(self.frame))

    def getSize(self):
        return self.totalSize

    def display(self):
        self.frame.show()
        print(str(self.frame) + "\n")

#put all of that stuff in an other class stringModifier
    def getFlipedPayload(self, positionList):
        flippedPayload=BitArray(bytes=self.payload)
        flippedPayload.invert(positionList)
        


