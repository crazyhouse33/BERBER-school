#!/usr/bin/python3
from packetSender import PacketSender
from supervisor import Supervisor
from finisher import Finisher

class Controller:
    def __init__(self, args):
        self.args=args

    def run(self):
        args=self.args
        headerSize = args.headerSize
        payloadSize = args.payloadSize
        BER = args.BER
        fileSize = args.fileSize
        
        sender = PacketSender(headerSize, payloadSize)
        supervisor = Supervisor(sender, BER)
        
        # should be in a separated class?
        numberOfPacket, lastSize = divmod(fileSize, payloadSize)
        cpt = numberOfPacket
        while cpt > 0:
            cpt -= 1
            supervisor.send()
        # send last packet
        if lastSize > 0:
            sender.setPacket(lastSize)
            supervisor.send()
            numberOfPacket += 1
        
        finisher = Finisher(supervisor, numberOfPacket, args)
        finisher.finish()
