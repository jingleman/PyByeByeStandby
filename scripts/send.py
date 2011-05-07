#!/usr/bin/python
# recv.py

import sys
import time
from socket import socket, AF_INET, SOCK_DGRAM

HOST = "10.0.2.155"
PORT = 53008

s = socket(AF_INET, SOCK_DGRAM)

s.sendto("D:1A03:E", (HOST, PORT))


sys.exit()

for h in range(ord("A"), ord("H")+1):
    for u in range(0, 16):
        cmd = "D:0%s%02d:E" % (chr(h), u)
        print cmd
        s.sendto(cmd, (HOST, PORT))
        time.sleep(0.1)
