import random
import packets.scapyPacket
from supervisor import Supervisor


class BitWiseSupervisor(Supervisor):
    """Create and use a PacketSender to luanch packet and actually computes statistics"""

    def __init__(self, BER)
        Supervisor(self, BER)
        self.oldCrc = -1

    def send(self):
        # send it once
        self.byteCount += self.packet.send()
        self.numberOfPacket += 1
        while True:
            # if failure resend it
            randFloat = random.uniform(0, 1)
            if randFloat < self.chanceOfPacketFailure():
                self.byteCount += self.packet.sendErroned()
                self.packetFailure += 1
            else:
                return

    def checkError(self, newcrc):
        return self.oldCrc == newcrc
