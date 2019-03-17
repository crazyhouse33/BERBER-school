from scapy.all import Raw, Ether, IP, UDP, sendp
from senders.sender import Sender
from bitstring import BitArray
import crcmod

class ScapySender(Sender):

    def __init__(self, headerSize, iface):
        super().__init__(headerSize, iface )

        self.IP_DST_ADDRESS = "127.0.0.1"
        self.UDP_PORT = 26381
        self.baseTrame = BitArray(bytes( Ether() / IP(dst=self.IP_DST_ADDRESS) / UDP(sport=self.UDP_PORT, dport=self.UDP_PORT + 1)))

        self.crc32_func = crcmod.mkCrcFun(
            0x104c11db7,
            initCrc=0,
            xorOut=0xFFFFFFFF)  # preparing checksum computation

        neededArtificialHeader= headerSize - len(self.baseTrame.bytes)-4
        if neededArtificialHeader >0:
            headerToAppend= neededArtificialHeader * 'X'
            self.baseTrame.append(BitArray(bytes(Raw(headerToAppend))))
        elif neededArtificialHeader <0:
            exit("The minimal number of bytes your system send to use UDP over IP over Ether is greater than the headerSize you specified:\nspecified: "+ str(headerSize)+ '\nmin: ' + str(headerSize-neededArtificialHeader))

            


    def send(self):
        """send loaded packet"""
        sendp(Raw(self.trame.bytes), verbose=0, iface= self.iface)
        return self.totalSize



# sendErronned is not supposed to alter target payload. to ecnonomise the
# copy we just flip back altered bits at the end
        self.flipBit(int(self.totalSize / 2))
        return self.totalSize

    def setPayload(self, payload):
        self.flippedBit=[]
        self.payloadSize = len(payload)
        payload = Raw(load=payload)
        self.trame = BitArray(self.baseTrame)
        self.trame.append( BitArray(bytes(payload)) )
        self.initialCheckSum = self.getFCS()

#        print ("before check:",self.trame, "check=", self.initialCheckSum)
        self.trame.append(BitArray(self.initialCheckSum.to_bytes(4, 'little')))
#       print ("after check:",self.trame)
        self.computeTotalSize()
        return self.initialCheckSum

    def getFCS(self):
        #compute checksum, ignoring cut last bytes
        currentCheksum = self.crc32_func(self.trame.bytes)
        return currentCheksum

    def computeTotalSize(self):
        self.totalSize = len(self.trame.bytes)

    def flipBit(self, position):
        self.flippedBit.append(position)
        self.trame.invert(position)


#needed for bitwise stuff section

    def unflip(self):
        """reset the frame to match the initial one"""
        for i in self.flippedBit:
            self.trame.invert(i)
        self.flippedBit=[]

    def checkIfErronned(self):
        """return true if the current frame checksum match the initial one"""
        currentCheksum = self.crc32_func(self.trame.bytes[:-4])#ignoring initialchecksum
        return (currentCheksum != self.initialCheckSum)
