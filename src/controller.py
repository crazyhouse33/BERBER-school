#!/usr/bin/python3
from supervisor import Supervisor
from simulations.noPacket import NoPacketSimulation
from simulations.sendTrueFile import TrueFileSimulation
import os


class Controller:

    def __init__(self, args):
        self.args = args
        self.supervisor = Supervisor(args.BER)
        if (args.simuled):
            self.simulation = NoPacketSimulation(self.supervisor, args)
        else:
            if not self.IAmRoot():
                exit("Scapy need root privileges to open raw socket. Exiting.")
            self.simulation = TrueFileSimulation(self.supervisor, args)

    def run(self):
        self.simulation.preRun()
        self.simulation.run()
        self.simulation.terminate()

    def IAmRoot(self):
        return os.geteuid() == 0
