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
anyThing = "[^ ]*"

toTestNumericScenarios = ('random', 'randomF')
toTestSupervisors = ('bit', 'packet')
toTestModes = ('scapy', 'socket', 'simulated')


class TestBlackBox(unittest.TestCase):
    """Dont use subprocess and main, otherwise the imports overhead is enormous, fake a parser instead"""

    def testQuick(self):
        # udp over ip over ethernet case
        for scenario in toTestNumericScenarios:
            for mode in toTestModes:
                for supervisor in toTestSupervisors:
                    self.blackBoxTest(
                        '-q -m ' + mode + ' -e ' + supervisor +
                        ' -s ' + scenario + ' 10000 0',
                        '10000 0.0 1468 10322 ' +
                        anyFloat)
                    self.blackBoxTest(
                        '-q -m ' + mode + ' -e ' + supervisor +
                        ' -s ' + scenario + ' -a 10000 0.001',
                        5 * anyThing)

    def testDelayed(self):
        print('testing non 0 delayed mode')
        delayed = 0.2
        result = self.getResult(
            '-q -m ' +
            'simulated -e bit -P 1 -s randomF ' +
            '-d ' +
            str(delayed) +
            ' 2 0')['result']

        result = result.split(' ')
        time = result[3]
        timeFloat = float(time)
        self.assertGreater(timeFloat, delayed)

    def blackBoxTest(self, command, expected):
        print('testing: ' + command)

        regexp = re.compile(expected)

        resultDict = self.getResult(command)
        result = resultDict['result']

        doResultMatchExpected = regexp.match(result)
        if doResultMatchExpected is None:
            self.fail(
                'the scenario result do not match the expected one:\ngot        ' +
                result +
                '\nexpected: ' +
                expected)
        self.assertTrue(doResultMatchExpected)

        self.bonusTests(resultDict['args'], resultDict['controller'])
        return result

    def getResult(self, command):
        command = command.split(' ')
        parser = Parser()
        args = parser.parse(command)

        controller = Controller(
            args.ber,
            args.data,
            args.delayed,
            args.payloadSize,
            args.headerSize,
            args.quiet,
            args.scenario,
            args.supervisor,
            args.mode,
            args.iface,
            args.adaptative,
            args.maxTrame)

        sys.stdout = tmpStdOut = io.StringIO()
        controller.run()
        sys.stdout = sys.__stdout__
        return {
            'args': args, 'result': tmpStdOut.getvalue(), 'controller': controller}

    def bonusTests(self, args, controller):
        """test a controller in terminated state. """
        supervisor = controller.chosenScenario.supervisor
        scenario = controller.chosenScenario
        sender = controller.chosenSender


if __name__ == '__main__':
    unittest.main()
