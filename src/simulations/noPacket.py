from packets.simulationPacket import SimulationPacket
class NoPacketSimulation:
    def __init__(self,supervisor, args):
        self.packet = SimulationPacket(args.headerSize, args.payloadSize)
        supervisor.fileSize = int(args.filePath)


        supervisor.setPacket(self.packet)
        self.supervisor= supervisor
        self.args=args

    def run(self):
        numberOfPacket, lastSize = divmod(int(self.args.filePath), self.args.payloadSize)
        cpt = numberOfPacket
        while cpt > 0:
            cpt -= 1
            self.supervisor.send()
        # send last packet
        if lastSize > 0:
            self.packet.setPacket(lastSize)
            self.supervisor.send()
            numberOfPacket += 1
        self.supervisor.numberOfPacket=numberOfPacket

    def terminate(self):
            # quiet Mode
            if (self.args.quiet):
                print (
                    self.supervisor.fileSize,
                    self.supervisor.getCount(),
                    self.args.BER)
            else:
                errors = self.supervisor.getErrors()
                print(
                    'Simulation terminated. It took',
                    self.supervisor.getCount(),
                    'bytes to send ',
                    self.supervisor.fileSize,
                    'bytes:\n\tPacket Sent: ',
                    self.supervisor.numberOfPacket + errors,
                    '\n\tPacket failure: ',
                    errors,
                )
