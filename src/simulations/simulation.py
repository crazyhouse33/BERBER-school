import abc
from abc import ABCMeta, abstractmethod  # strange error when removing that
import time


class Simulation(abc.ABC):
    """Abstract class for Simulations, dont forget to set up supervisor.fileSize and number in packet (TODO force that with interface)"""

    def __init__(self, supervisor, args):
        supervisor.setPacket(self.packet)
        self.supervisor = supervisor
        self.args = args

    def preRun(self):
        self.startTime = time.time()

    @abstractmethod
    def run(self):
        pass

    def terminate(self):
        t1 = time.time()
        timeTaken = str(1000 * (t1 - self.startTime))
        # quiet Mode
        if (self.args.quiet):
            print (
                self.supervisor.fileSize,
                self.args.BER,
                self.supervisor.getCount(),
                timeTaken,
            )
        else:
            errors = self.supervisor.getErrors()
            print(
                'Simulation terminated. It took',
                self.supervisor.getCount(),
                'bytes to send ',
                self.supervisor.fileSize,
                'bytes:\n\tPacket Sent: ',
                self.supervisor.numberOfPacket + errors,
                '\n\tPacket failure: ',
                errors,
                '\n\tTime: ' + timeTaken + 'ms'
            )


    """apply a BER on each bit of a binary byte string"""

    def BERonByte(self, BER, byte_bin):
        newbyte_bin = ""
        #BER = 0.005
        for bit in byte_bin:
            probability = random.random()  # float aléatoire entre 0 et 1
            if probability <= BER:
                if bit == '0':
                    bit = '1'
                elif bit == '1':
                    bit = '0'
            newbyte_bin += bit
        return newbyte_bin

    """apply BER on a packet"""

    def applyBERonPacket(self, BER, packet):
        packet_bytes = bytearray(bytes(packet, 'ascii'))
        for i in range(len(packet_bytes)):
            byte = packet_bytes[i]
            # transforme l'entier octet en string binaire (ex: 65 en 0b1000001)
            byte_bin = bin(byte)
            byte_bin = byte_bin[2:]  # supprime le 0b du string
            byte_bin = self.BERonByte(BER, byte_bin)
            str_bin = "0b"
            byte_bin = str_bin + byte_bin  # rajoute le 0b au string binaire
            byte = int(
                byte_bin,
                2)  # retransforme le string binaire en un octet entier
            packet_bytes[i] = byte
        packet = packet_bytes.decode("ascii")
        return packet
