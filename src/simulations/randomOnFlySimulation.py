from simulations.simulation import Simulation
import string
import random


class RandomOnFlySimulation(Simulation):
    """data is an int specifing how many random byte need to be sent"""

    def preRun(self):
        
        self.supervisor.fileSize = self.dataToSend
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
    """
    TODO Benchmark against
    randomBytes= os.urandom(sizeOfString)
    return b64encode(randomBytes).decode('utf-8')
    """
