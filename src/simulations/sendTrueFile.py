from packets.scapy import ScapyPacket
class TrueFileSimulation:
    def __init__(self,supervisor, args):
        self.packet = ScapyPacket(args.headerSize, args.payloadSize)


        supervisor.setPacket(self.packet)
        self.supervisor= supervisor
        self.args=args

    def run(self):
        print(
            "Sending file functionnality is yet to implement, use -s for now")
        exit(0)




