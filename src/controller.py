#!/usr/bin/python3
from supervisor import Supervisor
from simulations.noPacket import NoPacketSimulation
from simulations.sendTrueFile import TrueFileSimulation
import time


class Controller:

    def __init__(self, args):
        self.args = args
        self.supervisor = Supervisor(args.BER)
        if (args.simuled):
            self.simulation = NoPacketSimulation(self.supervisor, args)
        else:
            self.simulation = TrueFileSimulation(self.supervisor, args)

    def run(self):
        self.simulation.run()
        self.simulation.terminate()
