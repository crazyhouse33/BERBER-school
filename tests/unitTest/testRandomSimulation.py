import unittest
import sys
sys.path.append("../../src/")

from simulations.randomSimulation import RandomSimulation
from supervisors.bitWiseSupervisor import BitWiseSupervisor


class TestRandomSimulation(unittest.TestCase):

    def testCreateData(self):
        print("\nTESTING data generation...")
        size = 120
        simul = RandomSimulation(0, 0, 0, 0)
        data = simul.getRandomString(size)

        print("\ngenerated data :")
        print(data)
        self.assertEqual(len(data), size)

    def testSplit(self):
        print("\nTESTING data splitting...\n")

        '''
        case size % splitSize = 0
        '''

        size = 100
        splitSize = 5
        simul = RandomSimulation(0, 0, 0, 0)
        data = simul.getRandomString(size)
        simul.splittedData = simul.split(data, splitSize)

        print("data :\n" + data + "\n")

        elemLengths = 0
        print("splitted data :")
        for i in simul.splittedData:
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)
        print("\n")

        self.assertEqual(
            len(simul.splittedData), float(size) / float(splitSize))
        self.assertEqual(elemLengths, len(data))
        self.splitIntegrityTest(data, simul.splittedData)

        print("-----\n")

        '''
        case size % splitSize != 0
        '''
        size = 100
        splitSize = 6
        simul = RandomSimulation(0, 0, 0, 0)
        data = simul.getRandomString(size)
        simul.splittedData = simul.split(data, splitSize)
        print("data :\n" + data + "\n")

        elemLengths = 0
        print("splitted data :")
        for i in simul.splittedData:
            print("[" + i + "]")
            elemLengths = elemLengths + len(i)

        print("\n")

        self.assertEqual(elemLengths, len(data))
        self.splitIntegrityTest(data, simul.splittedData)

    '''
    check if the concatenation of all elements of tab is equal to data
    '''

    def splitIntegrityTest(self, data, tab):
        concat = ""
        for elem in tab:
            concat += elem
        print("concatenated split : " + concat + "\n")
        self.assertEqual(concat, data)

if __name__ == '__main__':
    unittest.main()
