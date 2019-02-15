# BERBER-
usage: main.py [-h] [-P PAYLOADSIZE] [-H HEADERSIZE] [-F FILESIZE] [-q] [BER]

Simulation to observe the trade-of between small/large packet in non
negligeable BER environment. Defaults settings for Headers/Payload Size
correspond approxymately to UDP over IP over Ethernet scenario

./main.py -h for help

dependencies:
scapy: pip3 install scapy
bitstrings: pip3 install bitstrings

