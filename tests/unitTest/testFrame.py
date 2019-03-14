import unittest
import sys

sys.path.append("../../src/")
from packets.scapySender import ScapySender


class TestFrame(unittest.TestCase):

    def testPacketForging(self):
        print("TESTING PACKET FORGING...")
        
        payload = 'THISISTHEPAYLOAD'
        sender = ScapySender()
        sender.setPayload(payload)
        
        #self.assertEqual(str(sender.trame), str(b'\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00,\x00\x01\x00\x00@\x11|\xbe\x7f\x00\x00\x01\x7f\x00\x00\x01\x04\xd2\x04\xd2\x00\x18\xa8\xa3THISISTHEPAYLOAD'))
        
        expectedFrameSize = sender.getSize()
        realFrameSize = len(sender.trame.bytes)
        #print("real trame size (without Ethernet CRC) :\n" + str(realFrameSize) + " bytes / " + str(len(scapyFrame.frame)*8) + " bits\n")
        #print("expected trame size :\n" + str(scapyFrame.getSize()) + " bytes / " + str(scapyFrame.getSize()*8) + " bits")
        self.assertEqual(realFrameSize, expectedFrameSize)

if __name__ == '__main__':
    unittest.main()
