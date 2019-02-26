from scapy.all import *
import crcmod

class ScapyPacket:

    def __init__(self, payload):
        
        #sizes in bytes
        self.ETHERNET_HEADER_SIZE = 14
        self.IP_HEADER_SIZE = 20
        self.UDP_HEADER_SIZE = 8
        self.HEADER_SIZE = self.ETHERNET_HEADER_SIZE + self.IP_HEADER_SIZE + self.UDP_HEADER_SIZE
        self.IP_DST_ADDRESS = "127.0.0.1"
        self.UDP_PORT = 1234
        
        self.payloadSize = len(payload)
        self.fcsSize = 0
        
        self.payload = payload # !!! MODIFIED WHEN FRAME IS MANUALLY MODIFIED
        self.size = self.HEADER_SIZE + self.payloadSize + self.fcsSize
        
        self.frame = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:00:00:00:00:00")/IP(dst=self.IP_DST_ADDRESS, src="127.0.0.1")/UDP(sport=self.UDP_PORT, dport=self.UDP_PORT)/raw(self.payload)
        """/IP(dst=self.IP_DST_ADDRESS)/UDP(sport=self.UDP_PORT, dport=self.UDP_PORT)/raw(self.payload)"""
        self.fcs = self.calculateFCS()
        self.frame = self.frame
        
    def calculateFCS(self):
        frame_bytes = bytearray(bytes(str(self.frame), 'ascii'))
        crc32_func = crcmod.mkCrcFun(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)
        crc_hex = hex(crc32_func(frame_bytes))
        print("fcs : " + crc_hex)
        return crc_hex
        
    def send(self):
        """send loaded packet"""
        send(self.frame/raw(self.fcs), verbose=False)
        print(self.frame/raw(self.fcs))
        return self.size
    
    def getSize(self):
        return self.size
    
    
    def display(self):
        self.frame.show()
        print(str(self.frame) + "\n")
    
