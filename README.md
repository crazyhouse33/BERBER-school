# BERBER-
usage: main.py [-h] [-P PAYLOADSIZE] [-H HEADERSIZE] [-F FILESIZE] [-q] [BER]

Simulation to observe the trade-of between small/large packet in non
negligeable BER environment. Defaults settings for Headers/Payload Size
correspond approxymately to UDP over IP over Ethernet scenario

./main.py -h for help

dependencies:
#scapy: 
pip3 install scapy
#bitstrings: allow efficient representation and manipulation of binary data 
pip3 install bitstrings
#psutil: allow to retrieve and check stats about detected networkcard
pip3 install psutil 

#devStuff:
#pep8: autoformating of the code
pip3 install pep8
#unitest:
pip3 install unitest

