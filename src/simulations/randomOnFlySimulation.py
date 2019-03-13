from packets.scapyPacket import ScapyPacket
from simulations.simulation import Simulation
import string
import random


class RandomOnFlySimulation(Simulation):

    def __init__(self, supervisor, BER, payloadSize, headerSize, fileSize):
        self.packet = ScapyPacket()
        supervisor.fileSize = fileSize

        Simulation.__init__(self, supervisor, BER, payloadSize)

    def preRun(self):
        self.predictedNumberOfPacket, self.lastSize =divmod(
        self.supervisor.fileSize, self.payloadSize)
        self.cpt=self.predictedNumberOfPacket
        if self.lastSize>0:
            self.predictedNumberOfPacket+=1
        Simulation.preRun(self)
    
    def run(self):
        while self.cpt > 0:
            self.cpt -= 1
            self.packet.setPayload(self.getRandomString(self.payloadSize))
            self.supervisor.send()
        # send last packet
        if self.lastSize > 0:
            self.packet.setPayload(self.getRandomString(self.lastSize))
            self.supervisor.send()

    def getRandomString(self, sizeOfString):
        data = ""
        for x in range(sizeOfString):
            data += random.choice(string.hexdigits)
        return data
