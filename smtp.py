#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
    print("Usage: vrfy.py <userfile> <ip>")
    sys.exit(0)

s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((sys.argv[2], 25))
banner = s.recv(1024)
print(banner)
user = open(sys.argv[1], 'r')
for line in user.readlines():
    #VRFY
    s.send('VRFY ' + line)
    result = s.recv(1024)
    if result[0] == '2':
        print("[+] Found valid user: "+ result[-6:])
s.close()
