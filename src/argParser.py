import argparse

class Parser:
    """parse the arguments, TODO make only fileSize positional"""
    def parse(self):
        defaultPS=1454
        defaultHS=16
        defaultFS=10000
        defaultBER=0
        parser = argparse.ArgumentParser(description='Simulation to observe the trade-of between small/large packet in non negligeable BER environment. Defaults settings for Headers/Payload Size correspond approxymately to UDP over IP over Ethernet scenario')
        parser.add_argument('payloadSize', type=int, help='int specifying the size in Bytes of the packets payload. Default is '+ str(defaultPS), nargs='?', default=defaultPS)
        parser.add_argument('headerSize', type=int, help='int specifying the size in Bytes of the packets headers, Default is '+ str(defaultHS), nargs='?', default=defaultHS)
        parser.add_argument('fileSize', type=int, help='int specifying the size in Bytes of the total data to be sent, Default is '+ str(defaultFS), nargs='?', default=defaultFS)
        parser.add_argument('BER', type=float, help='float specifing the BER of the virtual network connexion'+ str(defaultBER), nargs='?', default=defaultBER)
        args = parser.parse_args()
        print("Simulation launched with :\n")
#FIXME the order is random for some reason (parse arg or namespace iteration?
        for arg in sorted(args.__dict__):
            print ("\t", arg,":",args.__dict__[arg])
        print()
        return args
