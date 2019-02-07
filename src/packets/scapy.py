class ScapyPacket:

    def __init__(self, headerSize, payloadSize):
        self.headerSize = headerSize
        self.payloadSize = payloadSize
        self.totalSize = headerSize + payloadSize

    def send(self):
        """send loaded packet"""
        return self.totalSize

    def sendErroned(self):
        self.send()

    def getSize(self):
        """return size of the current loaded Packet"""
        return self.totalSize

    def setPayload(self, newPayload):
        """Put a string as payload"""
        pass

    def computeTotalSize(self):
        self.totalSize = self.payloadSize + self.headerSize
