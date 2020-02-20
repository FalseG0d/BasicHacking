#!/usr/bin/python

import socket
from termcolor import colored

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host="127.0.0.1" #rawinput("[*] Enter the Host to scan: ")

def portscanner(port):
        if sock.connect_ex((host,port)):
                print(colored("[!!] Port %d is closed"%(port),'red'))
        else:
                print(colored("[*] Port %d is open"%(port),'green'))

for port in range(1,10000):
	portscanner(port)
