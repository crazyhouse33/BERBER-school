import os
import random
import string

os.chdir("../packets")
from scapyPacket import ScapyPacket
os.chdir("../simulations")

from simulation import Simulation


class randomSeriesSimulation:

    def __init__(self, dataSize, splitSize):
        self.data = self.createData(dataSize)
        self.splittedData = self.split(self.data, splitSize)

    
    '''create a string of random data of size bytes'''
    def createData(self, size):
        data = ""
        for x in range(size):
            data += random.choice(string.hexdigits)
        return data
    
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
    
