from frame import *

if  __name__ == "__main__" :
	
	
	payloadSize = 8
	payload = "01010101"
	
	scapyFrame = ScapyPacket(payloadSize, payload)
	scapyFrame.frame.show()
	
	#print(scapyFrame.frame.size())
