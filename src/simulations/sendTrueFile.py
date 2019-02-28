from packets.scapyPacket import ScapyPacket
from simulations.simulation import Simulation

from  os import path
from math import ceil


class TrueFileSimulation(Simulation):

    def __init__(self, supervisor, args):
        self.packet = ScapyPacket(args.headerSize)

        Simulation.__init__(self, supervisor, args)

    def preRun(self):
        try:
            self.fileToSend = open(self.args.filePath, 'r')
        except IOError as e:
            print ('Cannot open file', self.args.filePath + ':', e.strerror)
            exit(1)
        fileSize=path.getsize(self.args.filePath)
        self.supervisor.fileSize = fileSize
        self.predictedNumberOfPacket= ceil(fileSize/self.args.payloadSize)
        super().preRun()

    def run(self):
        while True:
            buff = self.fileToSend.read(self.args.payloadSize)
            if not buff:
                break
            self.packet.setPayload(buff)
            self.supervisor.send()
