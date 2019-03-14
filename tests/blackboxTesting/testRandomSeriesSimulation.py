import unittest
import sys
sys.path.append("../../src/")

from simulations.randomSeriesSimulation import RandomSeriesSimulation
from supervisor_robin import Supervisor_robin
from argParser import Parser


class TestRandomSeriesSimulation(unittest.TestCase) :
    
    def testCreateData(self):
        size = 20
        supervisor = Supervisor_robin(5, 42, size, 0.001, True, False, True)
        simul = RandomSeriesSimulation(supervisor)
    
        print("\nTESTING DATA GENERATION...")
        
        print("generated data : " + simul.data)
        self.assertEqual(len(simul.data), size)
        
    def testSplit(self):
        print("\nTESTING DATA SPLITTING...")
        
        '''
        case size % payloadLength = 0
        '''
        size = 100
        payloadLength = 5
        supervisor = Supervisor_robin(payloadLength, 42, size, 0.001, True, False, True)
        simul = RandomSeriesSimulation(supervisor)
        
        print("data :\n" + simul.data + "\n")
        
        elemLengths = 0
        print("splitted data :")
        for i in simul.splittedData :
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)
        print("\n")
        
        self.assertEqual(len(simul.splittedData), float(size)/float(payloadLength))
        self.assertEqual(elemLengths, len(simul.data))
        self.splitIntegrityTest(simul.data, simul.splittedData)
        
        '''
        case size % payloadLength != 0
        '''
        size = 100
        payloadLength = 6
        supervisor = Supervisor_robin(payloadLength, 42, size, 0.001, True, False, True)
        simul = RandomSeriesSimulation(supervisor)
        
        print("data :\n" + simul.data + "\n")
        
        elemLengths = 0
        print("splitted data :")
        for i in simul.splittedData :
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)
        
        self.assertEqual(elemLengths, len(simul.data))
        self.splitIntegrityTest(simul.data, simul.splittedData)
        
    
    '''
    check if the concatenation of all elements of tab is equal to data
    '''
    def splitIntegrityTest(self, data, tab):
        concat = ""
        for elem in tab:
            concat += elem
        print("data : " + data)
        print("concatenated split : " + concat + "\n")
        self.assertEqual(concat, data)
        
if __name__ == '__main__':
    unittest.main()
