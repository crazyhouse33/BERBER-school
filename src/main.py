#!/usr/bin/python3
import sys
from argParser import Parser
from controller import Controller

#TODO what is that?
sys.path.append("./src/")

parser = Parser()
args = parser.parse()


controller = Controller(args.ber, args.data, args.delayed, args.payloadSize, args.headerSize,  args.quiet, args.scenario, args.supervisor, args.mode, args.iface)
controller.run()
