from packets.scapySender import ScapySender
from simulations.simulation import Simulation

from  os import path
from math import ceil


class TrueFileSimulation(Simulation):

    def __init__(self, supervisor, filePath, BER,  payloadSize):
        self.filePath=filePath
        self.packet = ScapySender()

        Simulation.__init__(self, supervisor, BER, payloadSize)

    def preRun(self):
        self.fileToSend = open(self.filePath, 'r')
        fileSize=path.getsize(self.filePath)
        self.supervisor.fileSize = fileSize
        self.predictedNumberOfPacket= ceil(fileSize/self.payloadSize)
        super().preRun()

    def run(self):
        while True:
            buff = self.fileToSend.read(self.payloadSize)
            if not buff:
                break
            self.supervisor.setAndSend(buff)
