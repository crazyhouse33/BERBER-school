import unittest
import sys
sys.path.append("../../src/")

from simulations.randomSimulation import RandomSimulation
from supervisors.bitWiseSupervisor import BitWiseSupervisor

class TestRandomSimulation(unittest.TestCase) :
    
    def testCreateData(self):
        size = 20
        BER = 0
        interFrameDelay = 0
        supervisor = BitWiseSupervisor(BER, interFrameDelay)
        simul = RandomSimulation(supervisor, supervisor.BER, 10, 42, size)
        simul.data = simul.getRandomString(size)
        print("\nTESTING DATA GENERATION...")


        print("generated data : \n")
        print(simul.data)
        self.assertEqual(len(simul.data), size)
        
    def testSplit(self):
        print("\nTESTING DATA SPLITTING...")
        
        '''
        case size % payloadLength = 0
        '''
        payloadLength = 5
        size = 100
        supervisor = BitWiseSupervisor(0, 0)
        simul = RandomSimulation(supervisor, supervisor.BER, payloadLength, 42, size)
        simul.data = simul.getRandomString(size)
        simul.splittedData = simul.split(simul.data, payloadLength)


        
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
        supervisor = BitWiseSupervisor(0, 0)
        simul = RandomSimulation(supervisor, supervisor.BER, payloadLength, 42, size)
        simul.data = simul.getRandomString(size)
        simul.splittedData = simul.split(simul.data, payloadLength)
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
