from scapy.all import Raw, Ether, IP, UDP, sendp
from packets.packet import Packet
from bitstring import BitArray


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
        self.baseFrame = Ether() / IP(dst=self.IP_DST_ADDRESS) / UDP(sport=self.UDP_PORT, dport=self.UDP_PORT)

    def send(self):
        """send loaded packet"""
        sendp(self.frame, verbose=0, iface='lo' )
        return self.totalSize

    def sendErroned(self):
        bytesString = bytes(self.frame)

        bits = BitArray(bytesString)
        #TODO test it instead of printing it
        #print ('before\n', bits.bytes )
        bits.invert(int(self.totalSize/2))
        #print( 'after\n',bits.bytes)
        sendp(Raw(bits.bytes), verbose=0, iface='lo')
        return self.totalSize

    def setPayload(self, payload):
        self.payloadSize = len(payload)
        self.computeTotalSize()
        payload = Raw(load=payload)
        self.frame= self.baseFrame / payload

    def getSize(self):
        return self.totalSize

    def display(self):
        self.frame.show()
        print(str(self.frame) + "\n")
