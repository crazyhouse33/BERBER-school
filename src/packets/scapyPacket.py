from scapy.all import *
from packets.packet import Packet


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

    def send(self):
        """send loaded packet"""
#        send(self.frame)
        send(IP(src="10.0.99.100", dst="10.1.99.100") / ICMP() / "Hello World")
        return self.size

    def sendErroned(self):
        self.send()

    def setPayload(self, payload):
        self.payloadSize = len(payload)
        self.computeTotalSize()
        payload = Raw(load=payload)
        #self.frame = Ether() / IP(dst=self.IP_DST_ADDRESS) / UDP(port=self.UDP_PORT) / payload

        #print (str(self.frame))

    def getSize(self):
        return self.size

    def display(self):
        self.frame.show()
        print(str(self.frame) + "\n")
