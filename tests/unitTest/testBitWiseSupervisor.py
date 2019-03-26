import unittest
import sys

sys.path.append("../../src/")

from supervisors.bitWiseSupervisor import BitWiseSupervisor
from senders.scapySender import ScapySender
from simulations.randomSimulation import RandomSimulation


class testArgParser(unittest.TestCase):

    def testApplyBER(self):
        sender = ScapySender(46, "eth0")
        sender.totalSize = 1000

        simul = RandomSimulation(0, 0, 0)

        payload = simul.getRandomString(100)
        sender.setPayload(payload)
        print("payload tested : " + payload)
        supervisor = BitWiseSupervisor(sender, 0, 0)

        # ber is 0, frame must be clean
        self.assertFalse(supervisor.applyBER())

        sender.unflip()
        supervisor.BER = 1
        # ber is 1, frame must be wrong
        self.assertTrue(supervisor.applyBER())

if __name__ == '__main__':
    unittest.main()
