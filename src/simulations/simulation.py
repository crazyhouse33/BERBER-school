import abc
import time


class Simulation(abc.ABC):
    """Abstract class for Simulations"""

    def __init__(self, supervisor, args):
        supervisor.setPacket(self.packet)
        self.supervisor = supervisor
        self.args = args

    @abc.abstractmethod
    def run(self):
        self.startTime = time.time()

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
