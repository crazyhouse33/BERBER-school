import unittest
import sys

sys.path.append("../../src/")

from argParser import Parser
from controller import Controller

class testArgParser(unittest.TestCase):

    def testcheckbervalidity(self):
        print("TESTING BER validity...")
        controller = Controller(5, 42, "20", 0, True, False, True)
        #parser = Parser()
        ber = -1
        self.assertFalse(controller.checkbervalidity(ber))
        ber = 121921
        self.assertFalse(controller.checkbervalidity(ber))
        ber = 0
        self.assertTrue(controller.checkbervalidity(ber))
        ber = 1
        self.assertTrue(controller.checkbervalidity(ber))
        ber = 0.00043
        self.assertTrue(controller.checkbervalidity(ber))

    def testcheckpayloadsizevalidity(self):
        print("TESTING playload size validity...")
        controller = Controller(5, 42, "20", 0, True, False, True)
        #parser = Parser()
        payloadsize = -1
        self.assertFalse(controller.checkpayloadsizevalidity(payloadsize))
        payloadsize = 1600
        self.assertFalse(controller.checkpayloadsizevalidity(payloadsize))
        payloadsize = 0
        self.assertTrue(controller.checkpayloadsizevalidity(payloadsize))
        payloadsize = 1
        self.assertTrue(controller.checkpayloadsizevalidity(payloadsize))
        payloadsize = 20
        self.assertTrue(controller.checkpayloadsizevalidity(payloadsize))

if __name__ == '__main__':
    unittest.main()
