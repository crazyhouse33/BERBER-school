#!/usr/bin/python3
import argparse
from argParser import Parser
from packetSender import PacketSender
from supervisor import Supervisor
from finisher import Finisher

parser = Parser()
args = parser.parse()

headerSize = args.headerSize
payloadSize = args.payloadSize
BER = args.BER
fileSize=args.fileSize


sender = PacketSender(headerSize, payloadSize)
supervisor = Supervisor(sender, BER)

"""should be in a separated class?"""
numberOfPacket, lastSize= divmod(fileSize, payloadSize)
cpt=numberOfPacket
while cpt>0:
    cpt-=1
    supervisor.send()
"""send last packet"""
if lastSize > 0:
    supervisor.setPacket(lastSize)
    supervisor.send()
    numberOfPacket+=1

finisher = Finisher(supervisor, numberOfPacket, args)
finisher.finish()



