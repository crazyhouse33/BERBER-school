import unittest
import os

os.chdir("../../src/simulations")
from randomSeriesSimulation import *
os.chdir("../../tests/blackboxTesting")


class testRandomSeriesSimulation(unittest.TestCase) :
    
    def testSplit(self):
        print("TESTING DATA SPLITTING...")
        
        simul = randomSeriesSimulation(20, 4)
        
        print("data :\n" + simul.data + "\n")
        
        elemLengths = 0
        print("splitted data :")
        for i in simul.splittedData :
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)
        
        self.assertEqual(elemLengths, len(simul.data))
    
if __name__ == '__main__':
    unittest.main()
