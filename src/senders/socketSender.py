from scapy.all import Raw
from senders.scapySender import ScapySender
import socket
class SocketSender(ScapySender):

    def __init__(self,headerSize, iface):
        super().__init__(headerSize,iface)
        self.sock= socket.socket( socket.AF_PACKET,socket.SOCK_RAW)
        self.sock.bind(('lo',0))
        
    def send(self):
        self.sock.send(self.trame.bytes)
        return self.totalSize

    def die(self):
        self.sock.close()
