import random
import string
import crcmod

from packets.scapyPacket import ScapyPacket
from simulations.simulation_robin import Simulation_robin


class RandomSeriesSimulation(Simulation_robin):

    def __init__(self, supervisor):
        self.supervisor = supervisor
        self.ber = supervisor.args.ber
        
        self.dataSize = int(self.supervisor.args.filePath)
        self.data = self.createData(self.dataSize)
        
        self.payloadSize = self.supervisor.args.payloadSize
        self.splittedData = self.split(self.data, self.payloadSize)
    
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
            checksumBeforeBER = self.calculateFCS(frame)
            
            berFrame = self.applyBERonPacket(self.ber, frame)
            #print("BER packet :\n" + berPacket + "\n")
            checksumAfterBER = self.calculateFCS(berFrame)


            #TODO calculate checksum instead
           # error = (frame != berFrame)
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

    def calculateFCS(self, frame):
        frame_bytes = bytearray(bytes(frame, 'ascii'))
        crc32_func = crcmod.mkCrcFun(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)
        crc_hex = hex(crc32_func(frame_bytes))
        return crc_hex

    
