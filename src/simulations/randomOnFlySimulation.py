from packets.scapySender import ScapySender
from simulations.simulation import Simulation
import string
import random


class RandomOnFlySimulation(Simulation):

    def __init__(self, supervisor, BER, payloadSize, headerSize, fileSize):
        self.packet = ScapySender()
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
            self.supervisor.setAndSend(self.getRandomString(self.payloadSize))
        # send last packet
        if self.lastSize > 0:
            self.supervisor.setAndSend(self.getRandomString(self.lastSize))

    def getRandomString(self, sizeOfString):
        data = ""
        for x in range(sizeOfString):
            data += random.choice(string.hexdigits)
        return data
