#!/usr/bin/python3
from supervisors.supervisor import Supervisor
from supervisors.bitWiseSupervisor import BitWiseSupervisor
from simulations.noPacket import NoPacketSimulation
from simulations.sendTrueFile import TrueFileSimulation
from simulations.randomSimulation import RandomSimulation
from simulations.randomOnFlySimulation import RandomOnFlySimulation
import simulations

import threading
import time
import os
import logging

class Controller:

    def __init__(self, args):
        self.args = args
        self.emergencyStop=False
        if args.bitWise:
            self.supervisor = BitWiseSupervisor(args.BER, args.delayed)
        else:
            self.supervisor = Supervisor(args.BER, args.delayed)

        if (args.simuled):
            self.simulation = NoPacketSimulation(self.supervisor, args.BER, args.payloadSize, args.headerSize, int(args.filePath))
        else:
            if not self.IAmRoot():
                exit("Scapy need root privileges to open raw socket. Exiting.")
            if args.randomF:
                self.simulation = RandomOnFlySimulation(self.supervisor, args.BER, args.payloadSize, args.headerSize, int(args.filePath))
            elif args.random:
                self.simulation = RandomSimulation(self.supervisor, args.BER, args.payloadSize, args.headerSize, int(args.filePath))
            else:
                self.simulation = TrueFileSimulation(self.supervisor, args.filePath, args.BER, args.payloadSize)

    def run(self):
        try:
            if (not self.args.quiet):
                progressBarThread=threading.Thread(name='progressBarThread',target= self.threadFunction)
                progressBarThread.start()
            self.simulation.preRun()
            self.simulation.run()
        # avoiding progress bar waiting impact on the timer by delagating the join to the simulation 
        except BaseException as e:
            self.emergencyStop=True
            progressBarThread.join()
            logging.exception(e)
            exit(1)

        if (not self.args.quiet):
            self.simulation.terminate(progressBarThread,quiet=False)
        else:
            self.simulation.terminate(quiet=True)

    def threadFunction(self):
        while not self.emergencyStop and self.simulation.updateBar() :
            time.sleep(0.1)
        print ('\n')


    def IAmRoot(self):
        return os.geteuid() == 0
