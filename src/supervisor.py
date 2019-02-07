import random


class Supervisor:
    """Create and use a PacketSender to luanch packet and actually computes statistics"""

    def __init__(self, BER):
        self.byteCount = 0
        self.packetFailure = 0
        self.BER = BER

    def setPacket(self, packet):
        self.packet = packet

    def send(self):
        """When using scappy, just send the packet since error will be simulated in the subclasses"""
        while True:
            # send it once
            self.byteCount += self.packet.send()

            # if failure resend it
            randFloat = random.uniform(0, 1)
            if randFloat < self.chanceOfPacketFailure():
                self.byteCount += self.packet.sendErroned()
                self.packetFailure += 1
            else:
                return

    def chanceOfPacketFailure(self):
        return 1 - pow(1 - self.BER, self.packet.getSize())

    def getCount(self):
        return self.byteCount

    def getErrors(self):
        return self.packetFailure
