#!/usr/bin/python

import socket
import os
import sys

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s=socket.socket()
		s.connect((ip,port))
		banner=s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner,filename):
	f=open(filename,"r")
	for line in f.readlines():
		if line.strip("\n") in banner:
			print("[+] Server is vulnerable: "+banner.strip("\n"))
		else: 
			print("[-] No known Vulnerabilty was found")

def main():
	filename="Vulnabanners.txt"
	if len(sys.argv)>=2:
		if not os.path.isfile(filename):
			print "[-] File Doesnt Exist"
			exit(0)
		if not os.access(filename,os.R_OK):
			print("[-] Access Denied")
			exit(0)
	else:
		print("[-] Usage: "+str(sys.argv[0])+" ip address")
		exit(0)
	portlist=range(21,40)
	for ip in sys.argv:
		for port in portlist:
			banner=retBanner(ip,port)
			if banner:
				print("[+] "+ip+"/"+str(port))
				checkVulns(banner,filename)

main()
