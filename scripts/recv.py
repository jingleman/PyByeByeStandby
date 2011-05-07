#!/usr/bin/python -u
# recv.py
import sys
import datetime
import string
f = open('fulllog.txt', 'w')
s = open('state.txt', 'w')
outstr = datetime.datetime.now().strftime("%x %X ")
lastrecordedstate = "Startup"
currentstate = "Unknown"
matchfound = -1
from socket import *
u = socket(AF_INET,SOCK_DGRAM)
u.bind(('<broadcast>',53007))
while 1:
        outstr = datetime.datetime.now().strftime("%x %X ")
        d = u.recv(1024)
        if not d: break
        print d
# writing full output with timestamp to fulllog file
# stripping the first 30 chars: "BBSEM [id and ip]: " would be 32 if full xxx.xxx.xxx.xxx ip assigned
        f.write(outstr+d[30:]+'\n') 
# test for connection   
        matchfound = string.find(d, "Parsing |Z:OK:E|")
        if matchfound > -1:
                currentstate = "Connected"
# test for disconnection   
        matchfound = string.find(d, "Connecting to 88.208.205.87")
        if matchfound > -1:
                currentstate = "Disconnected"
# has state changed - write time of state change to state file
        if currentstate != lastrecordedstate:
                s.write(outstr+currentstate+'\n') 
                lastrecordedstate = currentstate
u.close()
