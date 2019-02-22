import random


class Supervisor_robin:

    def __init__(self, payloadSize, headerSize, filePath, ber, quiet, simulated, random):
        self.payloadSize = payloadSize
        self.headerSize = headerSize
        self.filePath = filePath
        self.ber = ber
        
        self.quiet = quiet
        self.simulated = simulated
        self.random = random
        
        self.byteCount = 0
        self.packetCount = 0
        self.wrongFrameCount = 0
        self.timeTaken = 0

    
    '''
    compute the total percent of wrong frames
    '''
    def computeErrorRate(self):
        return self.wrongFrameCount / self.packetCount * 100
