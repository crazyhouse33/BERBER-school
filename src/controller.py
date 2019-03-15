#!/usr/bin/python3
from supervisors.supervisor import Supervisor
from supervisors.bitWiseSupervisor import BitWiseSupervisor
from simulations.sendTrueFile import FileSimulation
from simulations.randomSimulation import RandomSimulation
from simulations.randomOnFlySimulation import RandomOnFlySimulation

from senders.socketSender import SocketSender
from senders.simulatedSender import SimulatedSender
from senders.scapySender import ScapySender
import simulations

import threading
import time
import os
import logging

class Controller:
    def __init__(self, BER, data, delayed, payloadSize, headerSize, quiet, scenario, supervisorString, mode):
        self.emergencyStop=False
        self.quiet=quiet

        chosenSender = self.instantiateSender(mode, headerSize)

        chosenSupervisor= self.instantiateSupervisor(supervisorString, chosenSender, BER, delayed)

        self.chosenScenario = self.instantiateScenario(scenario, chosenSupervisor, data, payloadSize)

    def instantiateSender(self, string, headerSize):
        if (string=='simulated'):
            return SimulatedSender(headerSize)

        #need-to-be-root limit
        #-------------------------------------------
        if not self.IAmRoot():
            exit("Scapy need root privileges to open raw socket. Exiting.")

        if (string=='socket'):
            return SocketSender(headerSize)
        if (string=='scapy'):
            return ScapySender(headerSize)
        exit("Error: this mode do not exist")

    def instantiateSupervisor(self, string, sender, BER, delayed):
        if (string == 'packet'):
            return Supervisor(sender, BER, delayed) 
        if (string == 'bit'):
            return BitWiseSupervisor(sender, BER, delayed)
        exit("Error: this supervisor do not exist")

    def instantiateScenario(self, string, supervisor, data, payloadSize):
        if (string=='file'):
            return FileSimulation(supervisor, data, payloadSize)
        elif (string=='random'):
            return RandomSimulation(supervisor, data, payloadSize)
        elif (string =='randomF'):
            return RandomOnFlySimulation(supervisor, data, payloadSize)
        exit("Error, this scenario do no exist")

                



    def run(self):
        try:
            if (not self.quiet):
                progressBarThread=threading.Thread(name='progressBarThread',target= self.threadFunction)
                progressBarThread.start()
            self.chosenScenario.preRun()
            self.chosenScenario.run()
        # avoiding progress bar waiting impact on the timer by delagating the join to the simulation 
        except BaseException as e:
            self.emergencyStop=True
            progressBarThread.join()
            logging.exception(e)
            exit(1)

        if (not self.quiet):
            self.chosenScenario.terminate(progressBarThread,quiet=False)
        else:
            self.chosenScenario.terminate(quiet=True)

    def threadFunction(self):
        while not self.emergencyStop and self.chosenScenario.updateBar() :
            time.sleep(0.1)
        print ('\n')


    def IAmRoot(self):
        return os.geteuid() == 0
