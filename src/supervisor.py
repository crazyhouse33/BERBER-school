import random


class Supervisor:

    def __init__(self, controller):
        self.controller = controller
        
        self.byteCount = 0
        self.packetCount = 0
        self.wrongFrameCount = 0
        self.timeTaken = 0

    
    '''
    compute the total percent of wrong frames
    '''
    def computeErrorRate(self):
        return self.wrongFrameCount / self.packetCount * 100
