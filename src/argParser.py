from argparse import ArgumentParser

import psutil#check existence of iface and mtu


class Parser:
    """parse the arguments, TODO make only fileSize positional"""
    def __init__(self):
        defaultPS = 1454
        defaultHS = 46
        defaultFS = 10000
        defaultDelay = 0
        defaultBER = 0
        defaultScenario= 'file'
        defaultSupervisor= 'bit'
        defaultMode='scapy'
        defaultIface='lo'
        self.parser = ArgumentParser(
            description='Simulation to observe the trade-off between small/large packet in non negligeable BER environment. Default settings for Headers/Payload Size correspond to UDP over IP over Ethernet scenario')

        self.parser.add_argument(
            '-P',
            '--payloadSize',
            type=int,
            help='int specifying the size in Bytes of the packets payload. Default is ' +
            str(defaultPS),
            default=defaultPS)

        self.parser.add_argument(
            '-H',
            '--headerSize',
            type=int,
            help='int specifying the size in Bytes of the packets headers, Default is ' +
            str(defaultHS),
            default=defaultHS)



        self.parser.add_argument(
            '-d',
            '--delayed',
            type=float,
            help='float specifing a minimum time in second to wait betwen 2 trames. Default is ' +
            str(defaultDelay) + 'WARNING: there is no way to simulate realistic interframe timing (nanosecond precision) because of thread sleeping precision in currents OS (milisecond precision)',
            default=defaultDelay
            )

        self.parser.add_argument(
            '-i',
            '--iface',
            type=str,
            help='str specifing the interface to be used for sending packet. Default is ' +
            str(defaultIface),
            default=defaultIface
            )
        
        self.parser.add_argument(
            '-s',
            '--scenario',
            type=str,
            help='string specifing wich scenario will be done. Default is Sending a file' +
            defaultScenario,
            default=defaultScenario,
            choices= ['file', 'string', 'random', 'randomF']
            )

        self.parser.add_argument(
            '-m',
            '--mode',
            type=str,
            help='string specifying the way packet are lunched. Default use scapy implementation' +
            defaultMode,
            default=defaultMode,
            choices= ['scapy', 'socket', 'simulated']
            )


        self.parser.add_argument(
            '-e',
            '--supervisor',
            type=str,
            help='string switching the way errors are simulated. Default is bitWise' +
            defaultSupervisor,
            default=defaultSupervisor,
            choices= ['bit', 'packet']
            )




        self.parser.add_argument("-q", '--quiet', help="decrease output verbosity",
                            action="store_true")

        self.parser.add_argument(
            'data',
            type=str,
            help='data to send. In simulated/random scenario, this argument is the size of the virtual file to be sent. a letter \'G\', \'M\' or \'K\' can be appended to specify a unit')

        self.parser.add_argument(
            'ber',
            type=float,
            help='float specifing the BER of the virtual network connexion. Default is ' +
            str(defaultBER),
            nargs='?',
            default=defaultBER)




    def parse(self, command=None):

        if command == None:
            self.args = self.parser.parse_args()
        #this is convenient for tests
        else:
            self.args= self.parser.parse_args(command)

        
        if (self.args.scenario == "random" or self.args.scenario == "randomF"):
            self.interpreteDataUnit()

        self.checkPayloadSize()
        self.checkData()
        self.checkPayloadSize()
        self.checkConflicts()
        self.checkIface()

        if (self.args.quiet == False):
            print("Simulation launched with :\n")
            for arg in sorted(self.args.__dict__): #need to sort it, otherwise the order is not deterministic
                print ("\t", arg, ":", self.args.__dict__[arg])
            print()
        return self.args
        
    def checkConflicts(self):
        if self.args.mode=='simulated' and self.args.supervisor=='bit':
            self.args.supervisor='packet'
            if self.args.quiet==False:
                print ('WARNING: autohandled conflict: simulated only made sense used with the packet supervisor')
    
    '''
    affect to self.data the effective value of data, after interpreting it with format <int><G/M/K>
    for gigabytes, megabytes, kilobytes or bytes
    '''
    def interpreteDataUnit(self):
        unit = self.args.data[-1]
        
        if (unit.isdigit()): #no letter in the end
            self.args.data = int(self.args.data)
        else:
            prefix = int(self.args.data[:-1])
            
            if (unit == 'G'):
                self.args.data = prefix * 1000000000
            elif (unit == 'M'):
                self.args.data = prefix * 1000000
            elif (unit == 'K'):
                self.args.data = prefix * 1000
            else:
                exit('Bad unit format: use G|M|K')
                

    def checkData(self):
        if type(self.args.data) is int:
            if self.args.data < 0:
                exit("Error: data is not valid, it must be a positive integer. Exiting")

    def checkBer(self):
        if self.args.ber < 0 or self.args.ber > 1:
            exit("Error: BER is not valid, it must be a float between 0 and 1. Exiting")

    def checkPayloadSize(self):
        if self.args.payloadSize < 0 :
            exit("Error: payloadSize is not valid, it must be a positive integer. Exiting")

    def checkIface(self):
        try:
            iface = psutil.net_if_stats()[self.args.iface]
        except:
            exit("Error: the interface specified do not exist. Exiting")



