import random
import packets.scapyPacket
import time


class Supervisor:
    """Create and use a PacketSender to luanch packet and actually computes statistics"""

    def __init__(self, BER, interFrameDelay):
        self.byteCount = 0
        self.numberOfPacket = 0
        self.packetFailure = 0
        self.BER = BER
        self.interFrameDelay = interFrameDelay

    def setPacket(self, packet):
        self.packet = packet

    def send(self):
        """When using scappy, just send the packet since error will be simulated in the subclasses"""
        # send it once
        self.numberOfPacket += 1
        while True:
            # if failure resend it
            randFloat = random.uniform(0, 1)
            if randFloat < self.chanceOfPacketFailure():
                self.byteCount += self.packet.sendErroned()
                self.afterSend()
                self.packetFailure += 1
            else:
                self.byteCount += self.packet.send()
                self.afterSend()
                return

    def afterSend(self):
        time.sleep(self.interFrameDelay)



    def chanceOfPacketFailure(self):
        return 1 - pow(1 - self.BER, self.packet.getSize())

    def getCount(self):
        return self.byteCount

    def getErrors(self):
        return self.packetFailure

