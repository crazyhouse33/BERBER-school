#!/usr/bin/python3
from packets.simulationPacket import SimulationPacket
from supervisor import Supervisor


class Controller:

    def __init__(self, args):
        self.args = args
# in simuled mode filePath become the size of the virtual file
        if (args.simuled):
            self.fileSize = args.filePath
            self.packet = SimulationPacket(args.headerSize, args.payloadSize)
        else:
            self.sendFileExperience()

        self.supervisor = Supervisor(self.packet, args.BER)

    def run(self):
        args = self.args
        headerSize = args.headerSize
        payloadSize = args.payloadSize
        filePath = args.filePath

        if (args.simuled):
            numberOfPacket = self.simuledExperience(filePath, payloadSize)
        else:
            self.sendFileExperience()

        self.terminate(numberOfPacket)

    def simuledExperience(self, fileSize, payloadSize):
        numberOfPacket, lastSize = divmod(fileSize, payloadSize)
        cpt = numberOfPacket
        while cpt > 0:
            cpt -= 1
            self.supervisor.send()
        # send last packet
        if lastSize > 0:
            self.packet.setPacket(lastSize)
            self.supervisor.send()
            numberOfPacket += 1
        return numberOfPacket

    def sendFileExperience(self):
        print(
            "Sending file functionnality is yet to implement, use -s for now")
        exit(0)

    def terminate(self, numberOfPacket, ):
        # quiet Mode
        if (self.args.quiet):
            print (
                self.args.fileSize,
                self.supervisor.getCount(),
                self.args.BER)
        else:
            errors = self.supervisor.getErrors()
            print(
                'Simulation terminated. It took',
                self.supervisor.getCount(),
                'bytes to send ',
                self.fileSize,
                'bytes:\n\tPacket Sent: ',
                numberOfPacket + errors,
                '\n\tPacket failure: ',
                errors,
            )


