# BERBER-
usage: main.py [-h] [-P PAYLOADSIZE] [-H HEADERSIZE] [-F FILESIZE] [-q] [BER]

Simulation to observe the trade-of between small/large packet in non
negligeable BER environment. Defaults settings for Headers/Payload Size
correspond approxymately to UDP over IP over Ethernet scenario

positional arguments:
  BER                   float specifing the BER of the virtual network
                        connexion0

optional arguments:
  -h, --help            show this help message and exit
  -P PAYLOADSIZE, --payloadSize PAYLOADSIZE
                        int specifying the size in Bytes of the packets
                        payload. Default is 1454
  -H HEADERSIZE, --headerSize HEADERSIZE
                        int specifying the size in Bytes of the packets
                        headers, Default is 16
  -F FILESIZE, --fileSize FILESIZE
                        int specifying the size in Bytes of the total data to
                        be sent, Default is 10000
  -q, --quiet           decrease output verbosity
