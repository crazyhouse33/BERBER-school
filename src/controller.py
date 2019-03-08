#!/usr/bin/python3
from supervisor import Supervisor
from simulations.noPacket import NoPacketSimulation
from simulations.randomSeriesSimulation import RandomSeriesSimulation
from simulations.sendTrueFile import TrueFileSimulation
import time

'''
interprete arguments and give them to the supervisor
! data argument in __init__ is not yet interpreted, it is a string with a letter in the end
'''
class Controller:

    def __init__(self, payloadSize, headerSize, data, ber, quiet, simulated, random):
        
        self.payloadSize = payloadSize
        self.headerSize = headerSize
        self.data = data
        self.ber = ber
        
        self.quiet = quiet
        self.simulated = simulated
        self.random = random
        
        self.data = self.interpreteData(self.data)
        self.supervisor = Supervisor(self)
        
        if (self.simulated):
            self.simulation = NoPacketSimulation(self.supervisor)
        else:
            if (self.random):
                self.simulation = RandomSeriesSimulation(self.supervisor)
            else:
                self.simulation = TrueFileSimulation(self.supervisor)

        if not self.checkargsvalidity():
            exit(1)
    
    '''
    return the effective value of data, after interpreting it with format <int><G/M/K>
    for gigabytes, megabytes, kilobytes or bytes
    '''
    def interpreteData(self, data):
        unit = data[-1]
        if (unit.isdigit()): #no letter in the end
            return int(data)
        prefix = int(data[:-1])
        if (unit == 'G'):
            return prefix * 1000000000
        if (unit == 'M'):
            return prefix * 1000000
        if (unit == 'K'):
            return prefix * 1000
        else:
            return -1
        
    def run(self):
        self.simulation.preRun()
        self.simulation.run()
        self.simulation.terminate()


    def checkargsvalidity(self):
        if self.random:
                if self.checkbervalidity(self.ber)\
                        and self.checkpayloadsizevalidity(self.payloadSize)\
                        and self.checkrandomdatavalidity(self.data):
                    return True
                else:
                    return False
        elif self.simulated:
            if self.checkbervalidity(self.ber) \
                    and self.checkpayloadsizevalidity(self.payloadSize):
                return True
            else:
                return False

    def checkrandomdatavalidity(self, data):
        print(data)
        if data < 0:
            print("Error data not valid, it must be a positive integer")
            return False
        return True

    def checkbervalidity(self, ber):
        if ber < 0 or ber > 1:
            print("Error ber not valid, it must be between 0 and 1")
            return False
        return True

    def checkpayloadsizevalidity(self, payloadSize):
        if payloadSize < 0 or payloadSize > 1472:
            print("Error payloadSize not valid, it must be between 0 and 1472")
            return False
        return True
