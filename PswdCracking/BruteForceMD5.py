#!/usr/bin/python3
#A simple brute forcer method to guess password in hashcode

from urllib.request import urlopen
import hashlib

def tryOpen(path):
	try:
		pass_file=open(path,"r")
		return pass_file
	except:
		print("[-] File not found!!")
		quit()

pass_hash=input("[*] Enter sha1 Hash value: ")
path=input("[*] Enter the path to password file: ")

pass_file=tryOpen(path)

for word in pass_file:
#	print("[*] Trying: "+word.strip("\n"))
	enc_word=word.encode("utf-8")
	md5digest=hashlib.md5(enc_word.strip()).hexdigest()

	if md5digest==pass_hash:
		print("[+] Password Found: "+word)
		exit(0)
	else:
		print("[-] Password not: "+word.strip("\n"))

print("Password not found in this list. Try another file")
