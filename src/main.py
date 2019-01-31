#!/usr/bin/python3
from argParser import Parser
from packetSender import PacketSender
from supervisor import Supervisor
from finisher import Finisher
from packetModifier import PacketModifier

parser = Parser()
args = parser.parse()

headerSize = args.headerSize
payloadSize = args.payloadSize
BER = args.BER
fileSize = args.fileSize

sender = PacketSender(headerSize, payloadSize)
modifier = PacketModifier(sender)
supervisor = Supervisor(sender, BER)

#should be in a separated class?
numberOfPacket, lastSize = divmod(fileSize, payloadSize)
cpt = numberOfPacket
while cpt > 0:
    cpt -= 1
    supervisor.send()
#send last packet
if lastSize > 0:
    modifier.setPacket(lastSize)
    supervisor.send()
    numberOfPacket += 1

finisher = Finisher(supervisor, numberOfPacket, args)
finisher.finish()
