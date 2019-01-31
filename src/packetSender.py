class PacketSender:
    """TODO use SCAPY here, we may frament this class according to the functionnement of scapy"""
    # Initializer / Instance attributes

    def __init__(self, headerSize, payloadSize):
        self.headerSize = headerSize
        self.payloadSize = payloadSize
        self.totalSize = headerSize + payloadSize

    def send(self):
        """send loaded packet"""
        return self.totalSize

    def getSize(self):
        """return size of the current loaded Packet"""
        return self.totalSize

    def setPacket(self):
        self.payloadSize = payloadSize
        self.computeTotalSize()

    def computeTotalSize(self):
        self.totalSize = self.payloadSize + self.headerSize
