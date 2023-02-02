#!/bin/python3

import socket
import sys

if len(sys.argv) != 3:
        print("Usage: vrfy.py <host IP> <username>")
        sys.exit(0)

host = sys.argv[1]
names = open(sys.argv[2])

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection = socket.connect((host,25))

banner = socket.recv(1024)

print(banner.decode('utf-8'))

for line in names:
    command = 'VRFY ' + line + '\r\n'
    socket.send(command.encode())
    result = socket.recv(1024)

    print(result.decode('utf-8'))


socket.close()