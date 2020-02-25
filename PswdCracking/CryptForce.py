#!/usr/bin/python3
# Crypt library of python encrypts a string according to a 'salt' value that we provide thus ecah time an encryption is made. We get a differt output

import crypt


def crackPass(cryptWord,path):
	salt=cryptWord[0:2]

	try:
		dictionary=open(path,"r")
	except:
		print("[-] Path not found!!")
		quit()

	for word in dictionary.readlines():
		word=word.strip('\n')
		if (cryptWord==word):
			print("[+] Password Found: "+word)
			return

	print("[-] Password Not Found")
def main():
	path=input("[*] Enter the path to the Password file: ")
	dpath=input("[*] Enter the path to the Dictionary file: ")

	try:
		passfile=open(path,"r")
	except:
		print("[-] Path not found!!")
		quit()
	for line in passfile.readlines():
		if ":" in line:
			user=line.split(":")[0]
			print("[*] Cracking Password for "+user+": ")
			cryptWord=line.split(":")[1].strip(' ').strip('\n')
			crackPass(cryptWord,dpath)

main()
