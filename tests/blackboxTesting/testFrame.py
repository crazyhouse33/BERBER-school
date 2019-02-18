from scapyPacket import *
from sys import *
import unittest

# ! launch as root !
class TestFrame(unittest.TestCase) :

    def testPacketForging(self) :
        print("TESTING PACKET FORGING...")
        
        payload = 'THISISTHEPAYLOAD'
        scapyFrame = ScapyPacket(payload)
        #scapyFrame.display()
        self.assertEqual(str(scapyFrame.frame), str(b'\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x08\x00E\x00\x00,\x00\x01\x00\x00@\x11|\xbe\x7f\x00\x00\x01\x7f\x00\x00\x01\x04\xd2\x04\xd2\x00\x18\xa8\xa3THISISTHEPAYLOAD'))
        
        expectedFrameSize = scapyFrame.getSize()
        realFrameSize = len(scapyFrame.frame)
        print("real frame size (without Ethernet CRC) :\n" + str(realFrameSize) + " bytes / " + str(len(scapyFrame.frame)*8) + " bits\n")
        print("expected frame size :\n" + str(scapyFrame.getSize()) + " bytes / " + str(scapyFrame.getSize()*8) + " bits")
        self.assertEqual(realFrameSize, expectedFrameSize)

if __name__ == '__main__':
    unittest.main()
