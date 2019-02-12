from ../../src/packets/scapyPacket import *
from sys import *

# ! launch as root !
if  __name__ == "__main__" :
	
	payload = 'THISISTHEPAYLOAD'
	print("payload : [" + str(payload) + "] - " + str(len(payload)) + " bytes")
	
	scapyFrame = ScapyPacket(payload)
	scapyFrame.display()
	
	print("real frame size (without Ethernet CRC) :\n" + str(len(scapyFrame.frame)) + " bytes / " + str(len(scapyFrame.frame)*8) + " bits\n")
	print("computed frame size :\n" + str(scapyFrame.getSize()) + " bytes / " + str(scapyFrame.getSize()*8) + " bits")
	
	scapyFrame.send()
	
	
