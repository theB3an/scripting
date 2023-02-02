#!/bin/bash

for ip in 10.11.1.{1..255}
do
	ping -c 1 -W 1 $ip &>/dev/null && echo "$ip is responding"
done
