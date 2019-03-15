import random
import time


class Supervisor:
    """Create and use a PacketSender to luanch packet and actually computes statistics"""

    def __init__(self, sender, BER, interFrameDelay):
        self.sender=sender
        self.byteCount = 0
        self.numberOfPacket = 0
        self.packetFailure = 0
        self.BER = BER
        self.interFrameDelay = interFrameDelay


    def send(self):
        """When using scappy, just send the packet since error will be simulated in the subclasses"""
        # send it once
        self.numberOfPacket += 1
        while True:
            # if failure resend it
            randFloat = random.uniform(0, 1)
            if randFloat < self.chanceOfPacketFailure():
                self.byteCount += self.sendErroned()

            else:
                self.byteCount += self.sender.send()
                self.afterSend()
                return

    def setPayload(self, payload):
            self.sender.setPayload(payload)

    def setAndSend(self, payload):
        """Syntaxic sugar to mask the machine of state nature of the Sender class"""
        self.sender.setPayload(payload)
        self.send()

    def sendErroned(self):
        """send eroned frame in purpose"""
        self.packet.flipBit(int(self.totalSize / 2))
        self.packet.send()
        self.afterSend()
        self.packetFailure += 1

    def afterSend(self):
        time.sleep(self.interFrameDelay)

    def chanceOfPacketFailure(self):
        return 1 - pow(1 - self.BER, self.sender.getSize())

    def getCount(self):
        return self.byteCount

    def getErrors(self):
        return self.packetFailure

