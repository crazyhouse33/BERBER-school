import abc
from abc import ABCMeta, abstractmethod  # strange error when removing that
import time


class Simulation(abc.ABC):
    """Abstract class for Simulations, dont forget to set up supervisor.fileSize and number in packet (TODO force that with interface)"""

    def __init__(self, supervisor, dataToSend, payloadSize, adaptative):
        self.supervisor = supervisor
        self.dataToSend = dataToSend
        self.payloadSize = payloadSize
        if adaptative:
            self.bytesPerPacket = self.bytesPerPacketAdaptative

    def preRun(self):
        """extends this to set everything that need to be set( supervisor.fileSize, opening files...) before starting the timer"""
        # set end to the good value
        self.startTime = time.time()

    def bytesPerPacket(self):
        return self.payloadSize

    def bytesPerPacketAdaptative(self):
        return self.supervisor.getOptimalPacketSize()

    @abstractmethod
    def run(self):
        """If you want to be compatible with -a option, use bytesPerPacket when you iterate over the data to be sent"""
        pass

    def terminate(self, progressBarThread=None, quiet=False):
        t1 = time.time()
        timeTaken = str(1000 * (t1 - self.startTime))

        # if progressBarThread is running, need to wait him before printing
        # anything
        if progressBarThread is not None:
            progressBarThread.join()
        # quiet Mode
        if (quiet):
            print(
                self.supervisor.fileSize,
                self.supervisor.BER,
                self.payloadSize,
                self.supervisor.getCount(),
                timeTaken,
            )
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
                '\n\tTime: ' + timeTaken + 'ms'
            )
