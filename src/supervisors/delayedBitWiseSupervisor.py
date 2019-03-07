import random
import packets.scapyPacket
from supervisors.bitWiseSupervisor import BitWiseSupervisor
import time


class DelayedBitWiseSupervisor(BitWiseSupervisor):

    def __init__(self, BER, interFrameDelay):
        self.interFrameDelay = interFrameDelay
        BitWiseSupervisor.__init__(self, BER)

    def afterSend(self):
        time.sleep(self.interFrameDelay)


