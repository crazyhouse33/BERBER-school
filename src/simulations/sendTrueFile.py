from packets.scapyPacket import ScapyPacket
from simulations.simulation import Simulation

import os


class TrueFileSimulation(Simulation):

    def __init__(self, supervisor):
        self.supervisor = supervisor
        self.packet = ScapyPacket(self.supervisor.controller.headerSize, args.payloadSize)

        Simulation.__init__(self, self.supervisor)

    def preRun(self):
        try:
            self.fileToSend = open(self.supervisor.controller, 'r')
        except IOError as e:
            print ('Cannot open file', self.supervisor.controller.data + ':', e.strerror)
            exit(1)

        self.supervisor.fileSize = os.path.getsize(self.supervisor.controller.data)
        super().preRun()

    def run(self):
        numberOfPacket = 0
        while True:
            buff = self.fileToSend.read(self.supervisor.controller.payloadSize)
            if not buff:
                break
            self.packet.setPayload(buff)
            self.supervisor.send()
            numberOfPacket += 1
        self.supervisor.numberOfPacket = numberOfPacket
