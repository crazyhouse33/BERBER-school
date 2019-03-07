import random
import packets.scapyPacket
from supervisors.supervisor import Supervisor
import time


class DelayedSupervisor(Supervisor):

    def __init__(self, BER, interFrameDelay):
        self.interFrameDelay = interFrameDelay
        Supervisor.__init__(self, BER)

    def afterSend(self):
        time.sleep(self.interFrameDelay)


