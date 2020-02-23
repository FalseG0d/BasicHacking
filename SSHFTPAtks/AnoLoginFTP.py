#!/usr/bin/python

import ftplib

def anoLogin(hostname):
	try:
		ftp=ftplib.FTP(hostname)
		ftp.login("anonymous","anonymous")
		print("[+] "+hostname+" FTP Login Enabled.")
		ftp.quit()
	except Exception, e:
		print("[-] "+hostname+" FTP Annonymous Failed")

host=raw_input("[*] Enter the IP address: ")
anoLogin(host)

