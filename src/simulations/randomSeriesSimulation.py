from packets.scapyPacket import ScapyPacket
from simulations.simulation import Simulation

import os


class randomSeriesSimulation:

    def __init__(self, args):
        
        self.data = self.createData(args.filePath)
        self.splittedData = self.split(self.data)
        self.packet = ScapyPacket(payload)

        Simulation.__init__(self, supervisor, args)
        
        if self.testSplit("abcdefghijk", 2):
            print("testSplit OK")
    
    
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
    
    def testSplit(self, data, splitSize):
        print(data)
        array = self.split(data, splitSize)
        elemLengths = 0
        print("splitted data :")
        for i in array :
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)
        return elemLengths == len(data)
    
