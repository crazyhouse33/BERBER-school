import random
import string

from packets.scapyPacket import ScapyPacket
from simulations.simulation_robin import Simulation_robin


class RandomSeriesSimulation(Simulation_robin):

    def __init__(self, supervisor):
        self.supervisor = supervisor
        
        self.dataSize = int(self.supervisor.filePath)
        self.data = self.createData(self.dataSize)
        
        self.payloadSize = self.supervisor.payloadSize
        self.splittedData = self.split(self.data, self.payloadSize)
    
    '''
    start the simulation : create packets, apply BER and send it
    '''
    def run(self):
        i = 0
        print("Simulation launched...\n")
        while(i < len(self.splittedData)):
            
            payload = self.splittedData[i]
            
            packet = ScapyPacket(payload)
            #print("packet :\n" + str(packet.frame) + "\n")
            checksumBeforeBER = packet.calculateFCS()
            
            berPacket = ScapyPacket(payload)
            berPacket.frame = self.applyBERonPacket(self.supervisor.ber, str(berPacket.frame))
            #print("BER packet :\n" + berPacket + "\n")
            checksumAfterBER = berPacket.calculateFCS()
            
            error = (checksumBeforeBER != checksumAfterBER)
            #print("error : " + str(error) + "\n\n")
            
            packet.send()
            self.supervisor.byteCount += packet.getSize()
            self.supervisor.packetCount += 1
            
            if(error): #wrong frame, resend it
                self.supervisor.wrongFrameCount += 1
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

    
