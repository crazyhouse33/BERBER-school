from scapy.all import Raw, Ether, IP, UDP, sendp
from packets.packet import Packet
from bitstring import BitArray
from crcmod import mkCrcFun


class ScapyPacket(Packet):

    def __init__(self, headerSize):
        self.headerSize = headerSize

        # sizes in bytes
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
        self.baseFrame = Ether() / IP(dst=self.IP_DST_ADDRESS) / \
            UDP(sport=self.UDP_PORT, dport=self.UDP_PORT + 1)

        self.crc32_func = crcmod.mkCrcFun(
    0x104c11db7,
    initCrc=0,
     xorOut=0xFFFFFFFF)  # preparing checksum computation

    def send(self):
        """send loaded packet"""
        sendp(Raw(self.frame.bytes), verbose=0, iface='lo')
        return self.totalSize

    def sendErroned(self):

        # TODO test it instead of printing it
        # print ('before\n', bits.bytes )
        self.flipBit(int(self.totalSize / 2))
        # print( 'after\n',bits.bytes)
        sendp(Raw(self.frame.bytes), verbose=0, iface='lo')

# sendErronned is not supposed to alter target payload. to ecnonomise the
# copy we just flip back altered bits at the end
        self.flipBit(int(self.totalSize / 2))
        return self.totalSize

    def setPayload(self, payload):
        self.payloadSize = len(payload)
        self.computeTotalSize()
        payload = Raw(load=payload)
        self.frame = BitArray(  # translate the whole trame to binary
            bytes(
                self.baseFrame /
                payload
            )
            )
        crc=self.computeFCS()
        self.frame.append(crc)

    def sendErroned(self):
        self.send()

    def computeFCS(self):
        crc = crc32_func(self.frame.bytes)
        return crc

    def getSize(self):
        return self.totalSize

    def flipBit(self, position):
        self.frame.invert(position)
