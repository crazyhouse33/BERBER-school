from argparse import ArgumentParser


class Parser:
    """parse the arguments, TODO make only fileSize positional"""

    def parse(self):
        defaultPS = 1454
        defaultHS = 16
        defaultFS = 10000
        defaultBER = 0
        parser = ArgumentParser(
            description='Simulation to observe the trade-of between small/large packet in non negligeable BER environment. Defaults settings for Headers/Payload Size correspond approxymately to UDP over IP over Ethernet scenario')

        parser.add_argument(
            '-P',
            '--payloadSize',
            type=int,
            help='int specifying the size in Bytes of the packets payload. Default is ' +
            str(defaultPS),
            default=defaultPS)

        parser.add_argument(
            '-H',
            '--headerSize',
            type=int,
            help='int specifying the size in Bytes of the packets headers, Default is ' +
            str(defaultHS),
            default=defaultHS)

        parser.add_argument(
            'filePath',
            type=str,
            help='Path to the file to be send. In simuled mode, this argument is the size of the virtual file to be sent.')

        parser.add_argument(
            'BER',
            type=float,
            help='float specifing the BER of the virtual network connexion. Default is ' +
            str(defaultBER),
            nargs='?',
            default=defaultBER)

        parser.add_argument("-q", '--quiet', help="decrease output verbosity",
                            action="store_true")

        parser.add_argument("-s", '--simuled', help="do not send any packet",
                            action="store_true")
        
        parser.add_argument("-b", '--bitWise', help="apply ber on every individual bit. Slow",
                            action="store_true")


        args = parser.parse_args()
        if args.simuled:
            args.filePath = int(args.filePath)
        if (args.quiet == False):
            print("Simulation launched with :\n")
            for arg in sorted(args.__dict__):
                print ("\t", arg, ":", args.__dict__[arg])
            print()
        return args
