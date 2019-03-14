#!/usr/bin/python3
import sys
from argParser import Parser
from controller import Controller

sys.path.append("./src/")

parser = Parser()
args = parser.parse()

controller = Controller(args.payloadSize, args.headerSize,
                        args.data, args.ber, 
                        args.quiet, args.simulated, args.random)
controller.run()
