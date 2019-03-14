#!/usr/bin/python3
import sys
from argParser import Parser
from controller import Controller

sys.path.append("./src/")

parser = Parser()
args = parser.parse()


controller = Controller(args.ber, args.delayed, args.payloadSize, args.headerSize, args.data, args.bitWise, args.randomF, args.random, args.simulated, args.quiet)
controller.run()
