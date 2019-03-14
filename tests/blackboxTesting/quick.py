import unittest
import subprocess
import re  # regexp

anyFloat = "\d+\.\d+"


class TestBlackBox(unittest.TestCase):

    def testQuick(self):
        # udp over ip over ethernet case
        self.blackBoxTest(
            '../../src/main.py -q -s 10000 0',
            '10000 0.0 10294 ' +
            anyFloat)

        self.blackBoxTest(
            '../../src/main.py -s -q -H 1 -P 1 1000 0',
            '1000 0.0 2000 ' +
            anyFloat)

        self.blackBoxTest(
            '../../src/main.py -s -q -H 0 -P 1 1000 0',
            '1000 0.0 1000 ' +
            anyFloat)

    def blackBoxTest(self, command, expected):

        regexp = re.compile(expected)

        command = command.split(' ')
        process = subprocess.run(command, stdout=subprocess.PIPE)
        result = process.stdout.decode('utf-8')

        doResultMatchExpected = regexp.match(result)
        self.assertTrue(doResultMatchExpected)

if __name__ == '__main__':
    unittest.main()
