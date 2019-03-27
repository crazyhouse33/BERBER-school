from simulations.simulation import Simulation
import string
import random


class RandomOnFlySimulation(Simulation):
    """data is an int specifing how many random byte need to be sent"""

    def preRun(self):

        self.supervisor.fileSize = self.dataToSend
        self.cpt = self.supervisor.fileSize
        Simulation.preRun(self)

    def run(self):
        while self.cpt != 0:
            bytesToSend = self.bytesPerPacket()
            self.cpt -= bytesToSend
            # correct last packet size
            if self.cpt <= 0:
                bytesToSend += self.cpt
                self.cpt = 0
            self.supervisor.setAndSend(self.getRandomString(bytesToSend))

    def getRandomString(self, sizeOfString):
        data = ""
        for x in range(sizeOfString):
            data += random.choice(string.hexdigits)
        return data
    """
    TODO Benchmark against
    randomBytes= os.urandom(sizeOfString)
    return b64encode(randomBytes).decode('utf-8')
    """
