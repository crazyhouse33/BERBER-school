import unittest
import sys

sys.path.append("../../src/")

from controller import Controller
from supervisor import Supervisor
from simulations.randomSeriesSimulation import RandomSeriesSimulation

class TestSimulation(unittest.TestCase):

    def testBERonByte(self):
        print("TESTING BERonByte...")
        size = 20
        supervisor = Supervisor(Controller(5, 42, "20", 0, True, False, True))
        simul = RandomSeriesSimulation(supervisor)
        data = "o"
        data_bytes = bytes(data, 'utf-8')
        for byte in data_bytes:
            byte_bin = bin(byte)
            byte_bin = byte_bin[2:]
            byte_bin_after_BER = simul.BERonByte(0, byte_bin)
            self.assertEqual(byte_bin, byte_bin_after_BER)
            byte_bin_after_BER = simul.BERonByte(1, byte_bin)
            self.assertNotEqual(byte_bin, byte_bin_after_BER)

if __name__ == '__main__':
    unittest.main()
