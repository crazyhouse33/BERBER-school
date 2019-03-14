from argparse import ArgumentParser


class Parser:
    """parse the arguments, TODO make only fileSize positional"""

    def parse(self):
        defaultPS = 1472
        defaultHS = 16
        defaultFS = 10000
        defaultDelay = 0
        defaultBER = 0
        parser = ArgumentParser(
            description='Simulation to observe the trade-off between small/large packet in non negligeable BER environment. Default settings for Headers/Payload Size correspond to UDP over IP over Ethernet scenario')

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
            'data',
            type=str,
            help='Path to the file to be send. In simulated mode, this argument is the size of the virtual file to be sent. a letter \'G\', \'M\' or \'K\' can be appended to specify a unit')

        parser.add_argument(
            'ber',
            type=float,
            help='float specifing the BER of the virtual network connexion. Default is ' +
            str(defaultBER),
            nargs='?',
            default=defaultBER)

        parser.add_argument(
            '-d',
            '--delayed',
            type=float,
            help='float specifing a minimum time to wait betwen 2 trames. Default is ' +
            str(defaultDelay),
            default=defaultDelay)


        parser.add_argument("-q", '--quiet', help="decrease output verbosity",
                            action="store_true")

        parser.add_argument("-s", '--simulated', help="do not send any packet",
                            action="store_true")

        parser.add_argument("-rf", '--randomF', help="send random characters generated on the fly",
                            action="store_true")

        parser.add_argument("-r", '--random', help="send a randomly generated series of Bytes",
                            action="store_true")
        
        parser.add_argument("-b", '--bitWise', help="use bitwise stuf",
                            action="store_true")

        self.args = parser.parse_args()

        
        if self.args.simulated or self.args.random or self.args.randomF:
            self.args.data = self.interpreteData(self.args.data)
        if (self.args.quiet == False):
            print("Simulation launched with :\n")
            for arg in sorted(self.args.__dict__):
                print ("\t", arg, ":", self.args.__dict__[arg])
            print()
        return self.args
        
    
    '''
    return the effective value of data, after interpreting it with format <int><G/M/K>
    for gigabytes, megabytes, kilobytes or bytes
    '''
    def interpreteData(self, data):
        unit = data[-1]
        if (unit.isdigit()): #no letter in the end
            return int(data)
        prefix = int(data[:-1])
        if (unit == 'G'):
            return prefix * 1000000000
        if (unit == 'M'):
            return prefix * 1000000
        if (unit == 'K'):
            return prefix * 1000
        else:
            return -1

