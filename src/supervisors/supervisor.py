import random
import time


class Supervisor:
    """Create and use a PacketSender to luanch packet and actually computes statistics"""

    def __init__(self, sender, BER, interFrameDelay, maxTrame):
        self.sender = sender
        self.byteCount = 0
        self.numberOfPacket = 0
        self.packetFailure = 0
        self.BER = BER
        self.interFrameDelay = interFrameDelay
        self.payloadSended = 0
        self.maxTrame = maxTrame
        if interFrameDelay != 0:
            # doing that to avoid time.sleep(0), which arent impacting perf but
            # make the progress bar buggy
            self.afterSenderSend = self.afterSenderSendSleep

    def send(self):
        self.preSend()
        self.realSend()

    def setAndSend(self, payload):
        """Syntaxic sugar to mask the machine of state nature of the Sender class"""
        self.setPayload(payload)
        self.send()

    def realSend(self):
        """When using scapy, just send the packet since error will be simulated in the subclasses"""
        while True:
            # if failure resend it
            randFloat = random.uniform(0, 1)
            if randFloat < self.chanceOfPacketFailure():
                self.sendErroned()

            else:
                self.senderSend()
                return

    def setPayload(self, payload):
        self.sender.setPayload(payload)
        self.loadedPayloadSize = len(payload)

    def senderSend(self):
        # send primitive offered by Sender
        self.byteCount += self.sender.send()
        self.afterSenderSend()

    def sendErroned(self):
        """send erroned frame in purpose"""
        self.sender.flipBit(int(self.sender.totalSize / 2))
        self.senderSend()
        self.packetFailure += 1

    def afterSenderSendSleep(self):
        time.sleep(self.interFrameDelay)

    def afterSenderSend(self):
        pass

    def preSend(self):
        # record data sent
        self.numberOfPacket += 1  # only useful for stats
        self.payloadSended += self.loadedPayloadSize

    def chanceOfPacketFailure(self):
        return 1 - pow(1 - self.BER, self.sender.getSize())

    def getOptimalPacketSize(self):
        theoricalOptimum = self.theoricalPacketSize()
        if theoricalOptimum > self.maxTrame:
            return self.maxTrame
        else:
            return theoricalOptimum

    def theoricalPacketSize(self):
        return 1000

    def getCount(self):
        return self.byteCount

    def getErrors(self):
        return self.packetFailure
