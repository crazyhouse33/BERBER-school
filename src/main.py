#!/usr/bin/python3
import sys
from argParser import Parser
from controller import Controller

sys.path.append("./src/")

parser = Parser()
args = parser.parse()

controller = Controller(args)
controller.run()
