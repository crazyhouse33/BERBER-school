import unittest
import sys

sys.path.append("../../src/")

from argParser import Parser

class testArgParser(unittest.TestCase):

    def testcheckbervalidity(self):
        print("TESTING BER validity...")
        parser = Parser()
        ber = -1
        self.assertFalse(parser.checkbervalidity(ber))
        ber = 121921
        self.assertFalse(parser.checkbervalidity(ber))
        ber = 0
        self.assertTrue(parser.checkbervalidity(ber))
        ber = 1
        self.assertTrue(parser.checkbervalidity(ber))
        ber = 0.00043
        self.assertTrue(parser.checkbervalidity(ber))

    def testcheckpayloadsizevalidity(self):
        print("TESTING playload size validity...")
        parser = Parser()
        payloadsize = -1
        self.assertFalse(parser.checkpayloadsizevalidity(payloadsize))
        payloadsize = 1600
        self.assertFalse(parser.checkpayloadsizevalidity(payloadsize))
        payloadsize = 0
        self.assertTrue(parser.checkpayloadsizevalidity(payloadsize))
        payloadsize = 1
        self.assertTrue(parser.checkpayloadsizevalidity(payloadsize))
        payloadsize = 20
        self.assertTrue(parser.checkpayloadsizevalidity(payloadsize))

if __name__ == '__main__':
    unittest.main()