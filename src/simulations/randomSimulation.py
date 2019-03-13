import random
import string

from packets.scapyPacket import ScapyPacket
from simulations.randomOnFlySimulation import RandomOnFlySimulation


class RandomSimulation(RandomOnFlySimulation):
    """Same as RandomSimulation but do not generate random data on the fly, since the legends says it bother the client. Only God know why.
    We dont directely iterate over the string, but rather over an array of the splitted string. This is a other "Feature" asked by the client.
    """

    def __init__(self, supervisor, BER, payloadSize, headerSize, fileSize):
        super().__init__( supervisor, BER, payloadSize, headerSize, fileSize)
        data = self.getRandomString(fileSize)
        self.splittedData = self.split(data, payloadSize)

    '''
    start the simulation : create packets, apply BER and send it
    '''
    def run(self):
        for i in range(len(self.splittedData)):
            payload = self.splittedData[i]
            self.packet.setPayload(payload)
            self.supervisor.send()


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


