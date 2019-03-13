import abc


class Packet(abc.ABC):
    """Abstract class for each packets"""

    @abc.abstractmethod
    def send(self):
        """send loaded packet (whith the good ethernet checksum in the end of the data payload(to trick wiresharck and take the additional byte into account), return the size of the packet which had been sent"""
        pass

    @abc.abstractmethod
    def sendErroned(self):
        """send an erroned packet, return the size of the packet which had been sent"""
        pass

    def getSize(self):
        """return size of the current loaded Packet"""
        return self.totalSize

    def computeTotalSize(self):
        self.totalSize = self.payloadSize + self.headerSize
