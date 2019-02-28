#!/usr/bin/python3
from supervisors.supervisor import Supervisor
from supervisors.bitWiseSupervisor import BitWiseSupervisor
from simulations.noPacket import NoPacketSimulation
from simulations.sendTrueFile import TrueFileSimulation

import threading
import time
import os


class Controller:

    def __init__(self, args):
        self.args = args
        if args.bitWise:
            self.supervisor = BitWiseSupervisor(args.BER)
        else:
            self.supervisor = Supervisor(args.BER)

        if (args.simuled):
            self.simulation = NoPacketSimulation(self.supervisor, args)
        else:
            if not self.IAmRoot():
                exit("Scapy need root privileges to open raw socket. Exiting.")
            self.simulation = TrueFileSimulation(self.supervisor, args)

    def run(self):
        if (not self.args.quiet):
            progressBarThread=threading.Thread(name='tamere',target= self.threadFunction)
            progressBarThread.start()
        self.simulation.preRun()
        self.simulation.run()
        # avoiding progress bar waiting impact on the timer by delagating the join to the simulation 
        if (not self.args.quiet):
            self.simulation.terminate(progressBarThread)
        else:
            self.simulation.terminate()

    def threadFunction(self):
        while self.simulation.updateBar():
            time.sleep(0.1)


    def IAmRoot(self):
        return os.geteuid() == 0
