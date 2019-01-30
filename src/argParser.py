import argparse

class Parser:
    """parse the arguments"""
    def parse(self):
        parser = argparse.ArgumentParser(description='Simulation to observe the trade-of between small/large packet in non negligeable BER environment. Defaults settings for Headers/Payload Size correspond approxymately to UDP over IP over Ethernet scenario')
        parser.add_argument('payloadSize', type=int, help='int specifying the size in Bytes of the packets payload. Default is 1454', nargs='?', default=1454)
        parser.add_argument('headerSize', type=int, help='int specifying the size in Bytes of the packets headers, Default is 46', nargs='?', default=46)
        parser.add_argument('fileSize', type=int, help='int specifying the size in Bytes of the total data to be sent, Default is 10000000', nargs='?', default=10000000)
        parser.add_argument('BER', type=float, help='float specifing the BER of the virtual network connexion', nargs='?', default=0.2)
        args = parser.parse_args()
        print("Simulation launched with :\n")
        for arg in args.__dict__:
            print ("\t", arg,":",args.__dict__[arg])
        return args
