#!/bin/python3

import dns.resolver
import dns.query
import dns.zone
import sys

domain = sys.argv[1]

nameservers = dns.resolver.resolve(domain, 'NS')

for server in nameservers:
    resolved = dns.resolver.resolve(server.target, 'A')
    for ip in resolved:
        print("\n[+] Trying zone transfer with "+str(server.target))
        try:
            zone = dns.zone.from_xfr(dns.query.xfr(str(ip), domain))

            print("[+] Zone transfer worked!\nPrinting hosts:")
            for host in zone:
                print("\t"+str(host))
        except Exception as e:
            print("[-] "+str(server.target)+" refused zone transfer")
