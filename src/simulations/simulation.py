import abc


class Simulation(abc.ABC):
    """Abstract class for Simulations"""

    def __init__(self, supervisor, args):
        supervisor.setPacket(self.packet)
        self.supervisor = supervisor
        self.args = args

    @abc.abstractmethod
    def run(self):
        pass

    def terminate(self):
        # quiet Mode
        if (self.args.quiet):
            print (
                self.supervisor.fileSize,
                self.supervisor.getCount(),
                self.args.BER)
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
            )
