#!/usr/bin/python3
from supervisors.supervisor import Supervisor
from supervisors.bitWiseSupervisor import BitWiseSupervisor
from simulations.sendTrueFile import FileSimulation
from simulations.randomSimulation import RandomSimulation
from simulations.randomOnFlySimulation import RandomOnFlySimulation

from progressBar import ProgressBar

from senders.socketSender import SocketSender
from senders.simulatedSender import SimulatedSender
from senders.scapySender import ScapySender
import simulations

import threading
import time
import os
import logging
import ctypes


class Controller:

    def __init__(self, BER, data, delayed, payloadSize,
                 headerSize, quiet, scenario, supervisorString, mode, iface):
        self.emergencyStop = False
        self.quiet = quiet

        self.progressBar = ProgressBar(1, suffix='Complete')

        self.chosenSender = self.instantiateSender(mode, headerSize, iface)

        chosenSupervisor = self.instantiateSupervisor(
            supervisorString,
            self.chosenSender,
            BER,
            delayed)

        self.chosenScenario = self.instantiateScenario(
            scenario,
            chosenSupervisor,
            data,
            payloadSize)

    def instantiateSender(self, string, headerSize, iface):
        if (string == 'simulated'):
            return SimulatedSender(headerSize, iface)

        # need-to-be-root limit
        #-------------------------------------------
        if not self.IAmRoot():
            exit("Scapy needs root privileges to open raw socket. Exiting.")

        if (string == 'socket'):
            return SocketSender(headerSize, iface)
        if (string == 'scapy'):
            return ScapySender(headerSize, iface)
        exit("Error: this mode do not exist")

    def instantiateSupervisor(self, string, sender, BER, delayed):
        if (string == 'packet'):
            return Supervisor(sender, BER, delayed)
        if (string == 'bit'):
            return BitWiseSupervisor(sender, BER, delayed)
        exit("Error: this supervisor do not exist")

    def instantiateScenario(self, string, supervisor, data, payloadSize):
        if (string == 'file'):
            return FileSimulation(supervisor, data, payloadSize)
        elif (string == 'random'):
            return RandomSimulation(supervisor, data, payloadSize)
        elif (string == 'randomF'):
            return RandomOnFlySimulation(supervisor, data, payloadSize)
        exit("Error, this scenario do no exist")

    def run(self):
        try:
            if (not self.quiet):
                progressBarThread = threading.Thread(
                    name='progressBarThread',
                    target=self.threadFunction)
                progressBarThread.start()
            self.chosenScenario.preRun()
            self.progressBar.end = self.chosenScenario.predictedNumberOfPacket
            self.chosenScenario.run()
        # avoiding progress bar waiting impact on the timer by delagating the
        # join to the simulation
        except BaseException as e:
            self.emergencyStop = True
            if not self.quiet:
                progressBarThread.join()
            if (not isinstance(e, KeyboardInterrupt)):
                logging.exception(e)
            exit(1)
        finally:
            self.chosenSender.die()

        if (not self.quiet):
            self.chosenScenario.terminate(progressBarThread, quiet=False)
        else:
            self.chosenScenario.terminate(quiet=True)

    def threadFunction(self):
        while not self.emergencyStop and self.updateBar():
            time.sleep(0.1)
        print('\n')

    def IAmRoot(self):
        try:
            isAdmin = os.getuid() == 0
        except AttributeError:
            isAdmin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return isAdmin

    def updateBar(self):
        return self.progressBar.update(
            self.chosenScenario.supervisor.numberOfPacket)
