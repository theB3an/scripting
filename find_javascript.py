#!/bin/python

import sys
import re

javascript="[^/]*\.js"

file = open(sys.argv[1], "r")
file_list=re.findall(javascript, file.read())
file_list=set(file_list)
file_list=list(file_list)

print(file_list)