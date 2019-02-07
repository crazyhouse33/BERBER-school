import abc


class Packet(abc.ABC):
    """Abstract class for each packets"""

    @abc.abstractmethod
    def send(self):
        """send loaded packet, return the size of the packet"""
        pass

    @abc.abstractmethod
    def sendErroned(self):
        """send an erroned packet, return the size of the packet"""
        pass

    @abc.abstractmethod
    def getSize(self):
        """return size of the current loaded Packet"""
        pass

    @abc.abstractmethod
    def setPacket(self, payloadSize):
        """Set up Packet"""
        pass

    def computeTotalSize(self):
        self.totalSize = self.payloadSize + self.headerSize
