from packets.packet import Packet


class SimulationPacket(Packet):

    def __init__(self, headerSize, payloadSize):
        self.headerSize = headerSize
        self.payloadSize = payloadSize
        self.totalSize = headerSize + payloadSize

    def send(self):
        return self.totalSize

    def sendErroned(self):
        return self.send()

    def setPayload(self, payloadSize):
        self.payloadSize = payloadSize
        self.computeTotalSize()
