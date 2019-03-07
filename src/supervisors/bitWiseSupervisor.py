import random
import packets.scapyPacket
from supervisors.supervisor import Supervisor


class BitWiseSupervisor(Supervisor):
    """Create and use a PacketSender to luanch packet and actually computes statistics"""

    def __init__(self, BER, interFrameDelay):
        Supervisor.__init__(self,BER,interFrameDelay)

    def send(self):
        self.numberOfPacket += 1
        while True:
                erroned = self.applyBER()
                self.byteCount += self.packet.send()
                self.afterSend()
                if not erroned:
                    break
                self.packetFailure += 1
                self.packet.unflip()

    def applyBER(self):
        for i in range(self.packet.getSize()):
            randFloat = random.uniform(0, 1)
            if randFloat < self.BER:
                self.packet.flipBit(i)
        return self.packet.checkIfErronned()



