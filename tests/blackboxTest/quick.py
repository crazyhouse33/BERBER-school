import unittest
import subprocess
import re  # regexp
from cStringIO import StringIO
import sys
sys.path.append("../../src/")
from controller import Controller

anyFloat = "\d+\.\d+"


class TestBlackBox(unittest.TestCase):

    def testQuick(self):
        # udp over ip over ethernet case
        self.blackBoxTest(
            '2000 0 18 1472 42 True random bit scapy',
            '10000 0.0 10294 ' +
            anyFloat)

    def blackBoxTest(self, command, expected):

        regexp = re.compile(expected)

        command = command.split(' ')
        data = command[0]
        BER = command[1]
        delayed = command[2]
        payloadSize = command[3]
        headerSize = command[4]
        quiet = command[5]
        scenario = command[6]
        supervisorString = command[7]
        mode = command[8]
        controller = Controller(BER, data, delayed, payloadSize, headerSize, quiet, scenario, supervisorString, mode)
        sys.stdout = mystdout = StringIO()
        controller.run()
        sys.stdout = sys.__stdout__
        result = mystdout
        doResultMatchExpected = regexp.match(result)
        self.assertTrue(doResultMatchExpected)

if __name__ == '__main__':
    unittest.main()
