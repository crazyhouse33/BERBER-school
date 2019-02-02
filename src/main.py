#!/usr/bin/python3
from argParser import Parser
from controller import Controller

parser = Parser()
args = parser.parse()

controller = Controller(args)
controller.run()
