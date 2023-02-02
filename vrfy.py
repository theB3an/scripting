#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
        print("Usage: vrfy.py <username>")
        sys.exit(0)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection = socket.connect(('10.11.1.217',25))

banner = socket.recv(1024)

print(banner)

socket.send('VRFY ' + sys.argv[1] + '\r\n')
result = socket.recv(1024)

print(result)

socket.close()