import argparse


class Parser:
    """parse the arguments, TODO make only fileSize positional"""

    def parse(self):
        defaultPS = 1476
        defaultHS = 42
        defaultFS = 10000
        defaultBER = 0
        parser = argparse.ArgumentParser(
            description='Simulation to observe the trade-off between small/large packet in non negligeable BER environment. Defaults settings for Headers/Payload Size correspond approximately to UDP over IP over Ethernet scenario')

        parser.add_argument(
            '-P',
            '--payloadSize',
            type=int,
            help='integer specifying the size in Bytes of the packets payload. Default is ' +
            str(defaultPS),
            default=defaultPS)

        parser.add_argument(
            '-H',
            '--headerSize',
            type=int,
            help='integer specifying the size in Bytes of the packets headers. Default is ' +
            str(defaultHS),
            default=defaultHS)

        parser.add_argument(
            'data',
            type=str,
            help='Path to the file to be send. In simulated mode, this argument is the size of the virtual file to be sent.')

        parser.add_argument(
            'ber',
            type=float,
            help='float specifying the BER of the virtual network connexion. Default is ' +
            str(defaultBER),
            nargs='?',
            default=defaultBER)

        parser.add_argument("-q", '--quiet', help="decrease output verbosity",
                            action="store_true")

        parser.add_argument("-s", '--simulated', help="do not send any packet",
                            action="store_true")
        
        parser.add_argument("-r", '--random', help="use a random series of bytes",
                            action="store_true")

        args = parser.parse_args()

        '''TODO : tester la validité des arguments'''
        if self.checkargsvalidity(args):
            pass
        else:
            exit()

        if args.simulated:
            args.data = int(args.data)
        if (args.quiet == False):
            print("Simulation launched with :\n")
            for arg in sorted(args.__dict__):
                print ("\t", arg, ":", args.__dict__[arg])
            print()
        return args

    def checkargsvalidity(self, args):
        if self.checkbervalidity(args.ber) \
                and self.checkpayloadsizevalidity(args.payloadSize):
            return True
        else:
            return False

    def checkbervalidity(self, ber):
        if ber < 0 or ber > 1:
            print("Error ber not valid, it must be between 0 and 1")
            return False
        return True

    def checkpayloadsizevalidity(self, payloadSize):
        if payloadSize < 0 or payloadSize > 1472:
            print("Error payloadSize not valid, it must be between 0 and 1472")
            return False
        return True
