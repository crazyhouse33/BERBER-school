
class PacketModifier:
    """In the future, read file and set the packet payload accordingly"""

    def __init__(self, packetSender):
        self.packetSender = packetSender

    def setPacket(self, payloadSize):
        self.packetSender.payloadSize = payloadSize
