#!/bin/python3

import subprocess
import sys
start=int(sys.argv[2])
end=((int(sys.argv[3])+1))

for ip in range(start, end):
    address=sys.argv[1]+"."+str(ip)

    result=subprocess.call(['ping','-c','2','-W','3',address],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)

    if result==0:
        print (address)
    

