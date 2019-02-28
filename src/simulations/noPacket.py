from packets.simulationPacket import SimulationPacket
from simulations.simulation import Simulation


class NoPacketSimulation(Simulation):

    def __init__(self, supervisor, args):
        self.packet = SimulationPacket(args.headerSize, args.payloadSize)
        supervisor.fileSize = int(args.filePath)

        Simulation.__init__(self, supervisor, args)

    def preRun(self):
        self.predictedNumberOfPacket, self.lastSize =divmod(
            int(self.args.filePath), self.args.payloadSize)
        self.cpt=self.predictedNumberOfPacket
        if self.lastSize>0:
            self.predictedNumberOfPacket+=1
        Simulation.preRun(self)
    def run(self):
        while self.cpt > 0:
            self.cpt -= 1
            self.supervisor.send()
        # send last packet
        if self.lastSize > 0:
            self.packet.setPacket(self.lastSize)
            self.supervisor.send()
