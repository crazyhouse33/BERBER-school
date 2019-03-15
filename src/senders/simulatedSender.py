from senders.sender import Sender


class SimulatedSender(Sender):

    def send(self):
        return self.totalSize

    def sendErroned(self):
        return self.send()

    def setPayload(self, payload):
        self.payloadSize = len(payload)
        self.computeTotalSize()
