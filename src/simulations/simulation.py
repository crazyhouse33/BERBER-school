import abc
from abc import ABCMeta, abstractmethod  # strange error when removing that
import time


class Simulation(abc.ABC):
    """Abstract class for Simulations, dont forget to set up supervisor.fileSize and number in packet (TODO force that with interface)"""

    def __init__(self, supervisor, args):
        supervisor.setPacket(self.packet)
        self.supervisor = supervisor
        self.args = args

    def preRun(self):
        """extends this to set everything ( predictedNumberOfPacket before starting the timer"""
        self.progressBar= ProgressBar(self.predictedNumberOfPacket)
        self.startTime = time.time()

    @abstractmethod
    def run(self):
        pass

    def getPredictedNumberOfPacket(self):
        """needed for progress bar, need to set the value in the prerun"""
        return self.predictedNumberOfPacket

    def terminate(self):
        t1 = time.time()
        timeTaken = str(1000 * (t1 - self.startTime))
        # quiet Mode
        if (self.args.quiet):
            print (
                self.supervisor.fileSize,
                self.args.BER,
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
