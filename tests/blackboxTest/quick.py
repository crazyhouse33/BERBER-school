#!/usr/bin/python3
import unittest
import subprocess
import re  # regexp
import io
import sys
sys.path.append("../../src/")
from controller import Controller
from argParser import Parser
anyFloat = "\d+\.\d+"

toTestNumericScenarios = ('random', 'randomF')
toTestSupervisors = ('bit','packet')
toTestModes = ('scapy', 'socket', 'simulated') 

class TestBlackBox(unittest.TestCase):
    """Dont use subprocess and main, otherwise the imports overhead is enormous, fake a parser instead"""

    def testQuick(self):
# udp over ip over ethernet case
        for scenario in toTestNumericScenarios:
            for mode in toTestModes:
                for supervisor in toTestSupervisors:
                    self.blackBoxTest(
                        '-q -m ' + mode + ' -e '+ supervisor+ ' -s '+ scenario+ ' 10000 0',
                        '10000 0.0 10322 ' +
                        anyFloat)
                    """
                    self.blackBoxTest(

                        '-q -m ' + mode + ' -e '+ supervisor+ ' -s '+ scenario+ ' -H 1 -P 1 50 0',
                        '50 0.0 100 ' +
                        anyFloat)

                    self.blackBoxTest(
                        '-q -m ' + mode + ' -e '+ supervisor+ ' -s '+ scenario+ ' -H 0 -P 1 1000 0',
                        '1000 0.0 1000 ' +
                        anyFloat)
                    """
    def testDelayed(self):
        delayed=0.2
        result= self.getResult('-q -m ' + 'simulated -e bit -P 1 -s randomF '+ '-d '+ str(delayed)+ ' 2 0'
                        )
        result= result.split(' ')
        time = result[3]
        timeFloat=float(time)
        self.assertGreater(timeFloat,delayed)

    def blackBoxTest(self, command, expected):
        print('testing: '+ command)

        regexp = re.compile(expected)
        
        result= self.getResult(command)

        doResultMatchExpected = regexp.match(result)
        if doResultMatchExpected == None:
            self.fail('the scenario result do not match the expected one:\ngot        '+ result+ '\nexpected: '+ expected) 
        self.assertTrue(doResultMatchExpected)

        self.bonusTests(args, controller)
        return result

    def getResult(self,command):
        command = command.split(' ')
        parser = Parser()        
        args = parser.parse(command)

        controller = Controller(args.ber, args.data, args.delayed, args.payloadSize, args.headerSize,  args.quiet, args.scenario, args.supervisor, args.mode, args.iface)

        sys.stdout = tmpStdOut = io.StringIO()
        controller.run()
        sys.stdout = sys.__stdout__
        return tmpStdOut.getvalue()


    def bonusTests(self, args, terminatedController):
        """test aditional stuff thanks to supervisors stats. Not blackbox anymore"""
        pass

    

if __name__ == '__main__':
    unittest.main()
