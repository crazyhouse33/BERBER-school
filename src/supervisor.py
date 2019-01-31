import random
class Supervisor:
    """Create and use a PacketSender to luanch packet and actually computes statistics"""
    def __init__(self, sender, BER):
        self.byteCount=0
        self.packetFailure=0
        self.sender= sender
        self.BER= BER
        
        
    def send(self):
        """When using scappy, just send the packet since error will be simulated in the subclasses"""
        #send it once
        self.byteCount += self.sender.send()
        
        #if failure resend it
        randFloat=random.uniform(0, 1)
        if randFloat < self.chanceOfPacketFailure():
            self.packetFailure+=1
            """FIXME can reach recursion limit"""
            self.send()
        
    def chanceOfPacketFailure(self):
       return 1-pow(1-self.BER,self.sender.getSize())



    def setPacket(self, payloadSize):
        self.sender.payloadSize=payloadSize


    def getCount(self):
        return self.byteCount

    def getErrors(self):
        return self.packetFailure
        
