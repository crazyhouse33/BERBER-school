

class Finisher:

    def __init__(self, supervisor, numberOfPacket, args):
        self.supervisor = supervisor
        self.args = args
        self.numberOfPacket = numberOfPacket

    def finish(self):
        # quiet Mode
        if (self.args.quiet):
            print (
                self.args.fileSize,
                self.supervisor.getCount(),
                self.args.BER)
        else:
            errors = self.supervisor.getErrors()
            print(
                'Simulation terminated. It took',
                self.supervisor.getCount(),
                'bytes to send ',
                self.args.fileSize,
                'bytes:\n\tPacket Sent: ',
                self.numberOfPacket + errors,
                '\n\tPacket failure: ',
                errors,
            )
