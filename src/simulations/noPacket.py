from packets.simulationPacket import SimulationPacket
from simulations.simulation import Simulation


class NoPacketSimulation(Simulation):

    def __init__(self, supervisor):
        self.supervisor = supervisor
        self.packet = SimulationPacket(self.supervisor.controller.headerSize, self.supervisor.controller.payloadSize)
        supervisor.fileSize = int(self.supervisor.controller.data)

        Simulation.__init__(self, supervisor)

    def run(self):
        numberOfPacket, lastSize = divmod(
            int(self.supervisor.controller.data), self.supervisor.controller.payloadSize)
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
