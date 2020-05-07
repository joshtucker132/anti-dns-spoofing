import sys
import os
from scapy.all import *
from scapy.layers.dns import DNS, DNSRR

log = sys.argv[1]
os.chmod(log, 777)
print("processing " + log + "...")

packets = rdpcap(log)
for packet in packets:
    if packet.haslayer(DNS):
        ip = packet[DNSRR].rdata
        with open("blacklist.txt", 'r+') as blacklist:
        	if ip not in blacklist.read():
        		blacklist.write(ip + '\n')