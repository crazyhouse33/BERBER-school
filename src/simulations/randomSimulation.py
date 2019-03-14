import random
import string

from simulations.randomOnFlySimulation import RandomOnFlySimulation


class RandomSimulation(RandomOnFlySimulation):

    def __init__(self, supervisor, fileSize, payloadSize):
        super().__init__( supervisor, fileSize, payloadSize)

        data = self.getRandomString(fileSize)
        self.splittedData = self.split(data, payloadSize)

    '''
    start the simulation : create packets, apply BER and send it
    '''
    def run(self):
        for i in range(len(self.splittedData)):
            payload = self.splittedData[i]
            self.supervisor.setAndSend(payload)


    '''turn a series of data into an array of strings of size splitSize
    return the array of strings
    the last element may be less than splitSize long'''
    def split(self, data, splitSize):
        res = []
        index = 0
        while index < len(data) :
            nextElement = data[index:index+splitSize]
            res.append(nextElement)
            index = index + splitSize
        return res


