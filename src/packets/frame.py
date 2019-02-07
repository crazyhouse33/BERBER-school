from scapy.all import *

class ScapyPacket:

    def __init__(self, payloadSize, payload):
        
        ethernetHeaderSize = 112
        ipHeaderSize = 160
        udpHeaderSize = 64
        headerSize = ethernetHeaderSize + ipHeaderSize + udpHeaderSize
        checksumSize = 32
        
        self.payloadSize = payloadSize
        self.payload = payload
        self.size = headerSize + payloadSize + checksumSize
        
        self.frame = Ether()/IP()/UDP()/payload


    def send(self):
        """send loaded packet"""
        self.frame.send()
        return self.size


    def sendErroned(self):
        self.send()


    def setPayload(self, newPayload):
        """Put a string as payload"""
        pass
    
