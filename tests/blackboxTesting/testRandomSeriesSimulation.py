import unittest
import sys
sys.path.append("../../src/")

from simulations.randomSeriesSimulation import RandomSeriesSimulation


class testRandomSeriesSimulation(unittest.TestCase) :
    
    def testCreateData(self):
        size = 20
        print("\nTESTING DATA GENERATION...")
        simul = RandomSeriesSimulation(0, size, 4)
        data = simul.createData(size)
        print("generated data : " + data)
        self.assertEqual(len(data), size)
        
    def testSplit(self):
        print("\nTESTING DATA SPLITTING...")
        
        simul = RandomSeriesSimulation(0, 20, 4)
        
        print("data :\n" + simul.data + "\n")
        
        elemLengths = 0
        print("splitted data :")
        for i in simul.splittedData :
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)
        
        self.assertEqual(elemLengths, len(simul.data))
    
if __name__ == '__main__':
    unittest.main()
