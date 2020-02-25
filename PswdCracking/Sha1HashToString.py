#!/usr/bin/python3
#A simple brute forcer method to guess password in hashcode

from urllib.request import urlopen
import hashlib

sha1hash=input("[*] Enter Sha1 hash value: ")
passlist=str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt").read(),'utf-8')

for password in passlist.split("\n"):
	hashguess=hashlib.sha1(bytes(password,'utf-8')).hexdigest()

	if hashguess==sha1hash:
		print("[+] Password Found: "+ str(password))
		exit(0)
	else:
		print("[-] Password guess "+ str(password))

print("Password not found.")
