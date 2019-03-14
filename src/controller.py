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

    def __init__(self, ber, delayed, payloadSize, headerSize, data, bitWise, randomf, random, simulated, quiet):
        self.emergencyStop=False
        self.quiet=quiet
        if bitWise:
            self.supervisor = BitWiseSupervisor(ber, delayed)
        else:
            self.supervisor = Supervisor(ber, delayed)

        if (simulated):
            self.simulation = NoPacketSimulation(self.supervisor, ber, payloadSize, headerSize, data)
        else:
            if not self.IAmRoot():
                exit("Scapy need root privileges to open raw socket. Exiting.")
            if randomf:
                self.simulation = RandomOnFlySimulation(self.supervisor, ber, payloadSize, headerSize, data)
            elif random:
                self.simulation = RandomSimulation(self.supervisor, ber, payloadSize, headerSize, data)
            else:
                self.simulation = TrueFileSimulation(self.supervisor, data, ber, payloadSize)

    def run(self):
        try:
            if (not self.quiet):
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

        if (not self.quiet):
            self.simulation.terminate(progressBarThread,quiet=False)
        else:
            self.simulation.terminate(quiet=True)

    def threadFunction(self):
        while not self.emergencyStop and self.simulation.updateBar() :
            time.sleep(0.1)
        print ('\n')


    def IAmRoot(self):
        return os.geteuid() == 0
