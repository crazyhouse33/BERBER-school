from packets.simulationPacket import SimulationPacket
from simulations.simulation import Simulation


class NoPacketSimulation(Simulation):

    def __init__(self, supervisor, args):
        self.packet = SimulationPacket(args.headerSize, args.payloadSize)
        supervisor.fileSize = int(args.filePath)

        Simulation.__init__(self, supervisor, args)

    def run(self):
        numberOfPacket, lastSize = divmod(
            int(self.args.filePath), self.args.payloadSize)
        cpt = numberOfPacket
        while cpt > 0:
            cpt -= 1
            self.supervisor.send()
        # send last packet
        if lastSize > 0:
            self.packet.setPacket(lastSize)
            self.supervisor.send()
            numberOfPacket += 1
        self.supervisor.numberOfPacket = numberOfPacket
