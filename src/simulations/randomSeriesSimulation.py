import random
import string

from packets.scapyPacket import ScapyPacket
from simulations.simulation import Simulation


class RandomSeriesSimulation(Simulation):

    def __init__(self, ber, dataSize, splitSize):
        self.ber = ber
        self.data = self.createData(dataSize)
        self.splittedData = self.split(self.data, splitSize)
    
    '''
    start the simulation : create packets, apply BER and send it
    '''
    def run(self):
        i = 0
        while(i < len(self.splittedData)):
            
            payload = self.splittedData[i]
            packet = ScapyPacket(payload)
            
            frame = str(packet.frame)
            #print("packet :\n" + packet + "\n")
            
            berFrame = self.applyBERonPacket(self.ber, frame)
            #print("BER packet :\n" + berPacket + "\n")
            
            #TODO calculate checksum instead
            error = (frame != berFrame)
            #print("error : " + str(error) + "\n\n")
            
            packet.send()
            
            if(error): #wrong frame, resend it
                continue
            else: #right frame, go to next iteration
                i += 1
        
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
    
