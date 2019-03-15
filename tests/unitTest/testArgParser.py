import unittest
import sys

sys.path.append("../../src/")

from argParser import Parser, ArgumentParser
from controller import Controller

class testArgParser(unittest.TestCase):
    
    '''
    return True if the calling of function raises an exit, False otherwise
    '''
    def check(self, function):
        try:
            function()
        except(SystemExit):
            return False
        return True
    
    
    def testCheckBer(self):
        print("TESTING BER validity...")
        parser = Parser()
        parser.args = ArgumentParser().parse_args()
        
        parser.args.ber = -1
        self.assertFalse(self.check(parser.checkBer))
        
        parser.args.ber = 121921
        self.assertFalse(self.check(parser.checkBer))
        
        parser.args.ber = 0
        self.assertTrue(self.check(parser.checkBer))
        
        parser.args.ber = 1
        self.assertTrue(self.check(parser.checkBer))
        
        parser.args.ber = 0.00043
        self.assertTrue(self.check(parser.checkBer))
        
    def testCheckData(self):
        print("TESTING data validity...")
        parser = Parser()
        parser.args = ArgumentParser().parse_args()
        
        parser.args.data = 1
        self.assertTrue(self.check(parser.checkData))
        
        parser.args.data = 0
        self.assertTrue(self.check(parser.checkData))
        
        parser.args.data = -1
        self.assertFalse(self.check(parser.checkData))
        
        parser.args.data = 45
        self.assertTrue(self.check(parser.checkData))
        
        parser.args.data = 123456
        self.assertTrue(self.check(parser.checkData))
        
    def testCheckPayloadSize(self):
        print("TESTING playload size validity...")
        parser = Parser()
        parser.args = ArgumentParser().parse_args()
        
        parser.args.payloadSize = -1
        self.assertFalse(self.check(parser.checkPayloadSize))
        
        parser.args.payloadSize = 1600
        self.assertTrue(self.check(parser.checkPayloadSize))
        
        parser.args.payloadSize = 0
        self.assertTrue(self.check(parser.checkPayloadSize))
        
        parser.args.payloadSize = 1
        self.assertTrue(self.check(parser.checkPayloadSize))
        
        parser.args.payloadSize = 20
        self.assertTrue(self.check(parser.checkPayloadSize))
        
    def testInterpreteDataUnit(self):
        print("TESTING interpreting of data argument...")
        parser = Parser()
        parser.args = ArgumentParser().parse_args()
        
        parser.args.data = "5849"
        parser.interpreteDataUnit()
        self.assertEqual(parser.args.data, 5849)
        
        parser.args.data = "10K"
        parser.interpreteDataUnit()
        self.assertEqual(parser.args.data, 10000)
        
        parser.args.data = "42M"
        parser.interpreteDataUnit()
        self.assertEqual(parser.args.data, 42000000)
        
        parser.args.data = "254G"
        parser.interpreteDataUnit()
        self.assertEqual(parser.args.data, 254000000000)
        
        parser.args.data = "25Q"
        self.assertFalse(self.check(parser.interpreteDataUnit))
        
        parser.args.data = "1"
        parser.interpreteDataUnit()
        self.assertEqual(parser.args.data, 1)

if __name__ == '__main__':
    unittest.main()
