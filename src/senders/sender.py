import abc


class Sender(abc.ABC):
    """Abstract class for each packets"""

    def __init__(self, headerSize):
        self.headerSize=headerSize

    @abc.abstractmethod
    def send(self):
        """send loaded packet (whith the good ethernet checksum in the end of the data payload(to trick wiresharck and take the additional byte into account), return the size of the packet which had been sent"""
        pass

    def getSize(self):
        """return size of the current loaded Packet"""
        return self.totalSize

    def computeTotalSize(self):
        self.totalSize = self.payloadSize + self.headerSize

    def die(self):
        pass
