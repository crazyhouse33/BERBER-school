from scapy.all import *

class ScapyPacket:

    def __init__(self, payload):
        
        #sizes in bytes
        self.ETHERNET_HEADER_SIZE  = 14
        self.IP_HEADER_SIZE = 20
        self.UDP_HEADER_SIZE = 8
        self.HEADER_SIZE = self.ETHERNET_HEADER_SIZE + self.IP_HEADER_SIZE + self.UDP_HEADER_SIZE
        self.IP_DST_ADDRESS = "127.0.0.1"
        self.UDP_PORT = 1234
        
        self.payloadSize = len(payload)
        self.checksumSize = 4
        
        self.payload = payload
        self.size = self.HEADER_SIZE + self.payloadSize + self.checksumSize
        
        self.frame = Ether()/IP(dst=self.IP_DST_ADDRESS)/UDP(sport=self.UDP_PORT, dport=self.UDP_PORT)/raw(self.payload)


    def send(self):
        """send loaded packet"""
        send(self.frame)
        return self.size


    def getSize(self):
        return self.size
    
    
    def display(self):
        self.frame.show()
        print(str(self.frame) + "\n")
    
