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
        size = 20
        supervisor = Supervisor_robin(5, 42, size, 0.001, True, False, True)
        simul = RandomSeriesSimulation(supervisor)
    
        print("\nTESTING DATA SPLITTING...")
        
        print("data :\n" + simul.data + "\n")
        
        elemLengths = 0
        print("splitted data :")
        for i in simul.splittedData :
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)
        
        self.assertEqual(elemLengths, len(simul.data))
    
if __name__ == '__main__':
    unittest.main()
