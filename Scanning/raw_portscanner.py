#!/usr/bin/python

import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.setdefaulttimeout(1)

#host="192.168.1.4"
host=raw_input("[*] Enter the Host to scan: ")
port=int(raw_input("[*] Enter the port number: "))

def portscanner(port):
        if sock.connect_ex((host,port)):
                print("Port %d is closed"%(port))
        else:
                print("Port %d is open"%(port))

portscanner(port)
