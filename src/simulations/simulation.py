import abc
from abc import ABCMeta, abstractmethod  # strange error when removing that
from progressBar import ProgressBar
import time


class Simulation(abc.ABC):
    """Abstract class for Simulations, dont forget to set up supervisor.fileSize and number in packet (TODO force that with interface)"""

    def __init__(self, supervisor, dataToSend, payloadSize):
        self.supervisor = supervisor
        self.dataToSend=dataToSend
        self.payloadSize=payloadSize
        #initialize end to non zero value to avoid thread concurrency fail
        self.progressBar= ProgressBar(1, suffix='Complete')

    def preRun(self):
        """extends this to set everything ( predictedNumberOfPacket, files...) before starting the timer"""
        #set end to the good value
        self.progressBar.end=self.predictedNumberOfPacket
        self.startTime = time.time()

    @abstractmethod
    def run(self):
        pass

    def updateBar(self):
        return self.progressBar.update(self.supervisor.numberOfPacket)


    def getPredictedNumberOfPacket(self):
        """needed for progress bar, need to set the value in the prerun"""
        return self.predictedNumberOfPacket

    def terminate(self,progressBarThread=None,quiet=False):
        t1 = time.time()
        timeTaken = str(1000 * (t1 - self.startTime))

        #if progressBarThread is running, need to wait him before printing anything
        if progressBarThread!= None:
            progressBarThread.join()
        # quiet Mode
        if (quiet):
            print (
                self.supervisor.fileSize,
                self.supervisor.BER,
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



