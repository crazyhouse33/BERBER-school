from simulations.simulation import Simulation

from os import path
from math import ceil


class FileSimulation(Simulation):
    """data is a path to a file to be sent"""

    def preRun(self):
        self.fileToSend = open(self.dataToSend, 'r')
        fileSize = path.getsize(self.dataToSend)
        self.supervisor.fileSize = fileSize
        super().preRun()

    def run(self):
        while True:
            buff = self.fileToSend.read(self.bytesPerPacket())
            if not buff:
                break
            self.supervisor.setAndSend(buff)
