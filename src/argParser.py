from argparse import ArgumentParser


class Parser:
    """parse the arguments, TODO make only fileSize positional"""

    def parse(self):
        defaultPS = 1472
        defaultHS = 16
        defaultFS = 10000
        defaultDelay = 0
        defaultBER = 0
        defaultScenario= 'file'
        defaultSupervisor= 'bit'
        defaultMode='scapy'
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
            defaultScenario,
            default=defaultScenario,
            choices= ['file', 'string', 'random', 'randomF']
            )

        parser.add_argument(
            '-m',
            '--mode',
            type=str,
            help='string specifying the way packet are lunched. Default use scapy implementation' +
            defaultMode,
            default=defaultMode,
            choices= ['scapy', 'socket', 'simulated']
            )


        parser.add_argument(
            '-e',
            '--supervisor',
            type=str,
            help='string switching the way errors are simulated. Default is bitWise' +
            defaultSupervisor,
            default=defaultSupervisor,
            choices= ['bit', 'packet']
            )




        parser.add_argument("-q", '--quiet', help="decrease output verbosity",
                            action="store_true")

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


        self.args = parser.parse_args()

        self.interpreteData()

        self.checkPayloadSize()
        self.checkData()
        self.checkPayloadSize()
        self.checkConflicts()

        if (self.args.quiet == False):
            print("Simulation launched with :\n")
            for arg in sorted(self.args.__dict__):#need to sort it otherwise the order is not determinist
                print ("\t", arg, ":", self.args.__dict__[arg])
            print()
        return self.args
        
    def checkConflicts(self):
        print (self.args.scenario, self.args.supervisor)
        if self.args.mode=='simulated' and self.args.supervisor=='bit':
            self.args.supervisor='packet'
            print ('WARNING: regled conflict: simulated only made sense used with the packet supervisor')
    
    '''
    return the effective value of data, after interpreting it with format <int><G/M/K>
    for gigabytes, megabytes, kilobytes or bytes
    '''
    def interpreteData(self):
        if self.args.scenario== 'simulated' or self.args.scenario =='random' or self.args.scenario=='randomF':#if simulation just need a number
            unit = self.args.data[-1]
            prefix = int(self.args.data[:-1])
            if (unit.isdigit()): #if digit in the end
                self.args.data= int(self.args.data)
            elif (unit == 'G'):
                self.args.data = prefix * 1000000000
            elif (unit == 'M'):
                self.args.data= prefix * 1000000
            elif (unit == 'K'):
                self.args.data = prefix * 1000
            else:
                exit('Bad unit format: use G|M|K')
                

    def checkData(self):
        if type(self.args.data) is int:
            if self.args.data < 0:
                exit("Error: data is not valid, it must be a positive integer")
        #TODO else open file, and transmit it in data (simulation dont need to manage opening file anymore)

    def checkBer(self):
        if self.args.ber < 0 or ber > 1:
            exit("Error: BER is not valid. Must a float between 0 and 1")

    def checkPayloadSize(self):
        if self.args.payloadSize < 0 :
            exit("Error: payloadSize is not valid, it must be a positive integer")
