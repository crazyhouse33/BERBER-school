from scapy.all import Raw
from senders.scapySender import ScapySender
import socket
class SocketSender(ScapySender):

    def __init__(self,headerSize):
        super().__init__(headerSize)
        self.sock= socket.socket( socket.AF_PACKET,socket.SOCK_RAW)
        self.sock.bind(('lo',0))
        
    def send(self):
        """send loaded packet"""
        self.sock.send(self.trame.bytes)
        return self.totalSize

    