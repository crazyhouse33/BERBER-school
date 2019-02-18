import unittest
from randomSeriesSimulation import *

class testRandomSeriesSimulation(unittest.TestCase) :
    
    def testSplit(self):
        print("TESTING DATA SPLITTING...")
        
        data = "thisisthedatatosplit"
        splitSize = 4
        print("data :\n" + data + "\n")
        
        splittedData = split(data, splitSize)
        elemLengths = 0
        print("splitted data :")
        for i in splittedData :
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)
        
        self.assertEqual(elemLengths, len(data))
    
if __name__ == '__main__':
    unittest.main()
