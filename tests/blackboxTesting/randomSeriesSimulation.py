

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
    def createData(size):
        data = ""
        for x in range(size):
            data += random.choice(string.hexdigits)
        return data
    
    '''turn a series of data into an array of strings of size splitSize
    return the array of strings
    the last element may be less than splitSize long'''
def split(data, splitSize):
    res = []
    index = 0
    while index < len(data) :
        nextElement = data[index:index+splitSize]
        res.append(nextElement)
        index = index + splitSize
    return res

