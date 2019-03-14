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
            help='data to send. In simulated/random scenario, this argument is the size of the virtual file to be sent. a letter \'G\', \'M\' or \'K\' can be appended to specify a unit')

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
            help='float specifing a minimum time in second to wait betwen 2 trames. Default is ' +
            str(defaultDelay) + 'WARNING: there is no way to simulate realistic interframe timing (nanosecond precision) because of thread sleeping precision in currents OS (milisecond precision)',
            default=defaultDelay
            )
        
        parser.add_argument(
            '-s',
            '--scenario',
            type=str,
            help='string specifing wich scenario will be done. Default is Sending a file' +
            str(defaultPS),
            default=defaultPS,
            choices= ['file', 'string', 'random', 'randomF']
            )

        parser.add_argument(
            '-m',
            '--mode',
            type=str,
            help='string specifying the way packet are lunched. Default use scapy implementation' +
            str(defaultPS),
            default=defaultPS,
            choices= ['scapy', 'socket', 'simulated']
            )


        parser.add_argument(
            '-e',
            '--supervisor',
            type=str,
            help='string switching the way erros are simulated. Default is bitWise' +
            str(defaultPS),
            default=defaultPS,
            choices= ['bit', 'packet']
            )




        parser.add_argument("-q", '--quiet', help="decrease output verbosity",
                            action="store_true")


        self.args = parser.parse_args()
        
        
        if self.args.scenario or self.args.random or self.args.randomF:
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
    
    
    
    

''' CHECKING ARGS VALIDITY '''
    
    def checkargsvalidity(self):
        if self.args.random:
                if self.checkbervalidity(self.args.ber)\
                        and self.checkpayloadsizevalidity(self.args.payloadSize)\
                        and self.checkrandomdatavalidity(self.args.data):
                    return True
                else:
                    return False
        elif self.args.simulated:
            if self.checkbervalidity(self.args.ber) \
                    and self.checkpayloadsizevalidity(self.args.payloadSize):
                return True
            else:
                return False

    def checkrandomdatavalidity(self, data):
        print(data)
        if data < 0:
            print("Error data not valid, it must be a positive integer")
            return False
        return True

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
