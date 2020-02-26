#!/usr/bin/python3

import subprocess

def change_mac(interface,new_mac):
	subprocess.call(["sudo","ifconfig",interface,"down"])
	subprocess.call(["sudo","ifconfig",interface,"hw","ether"+new_mac])
	subprocess.call(["sudo","ifconfig",interface,"up"])

def main():
	interface=str(input("[*] Enter the Interface you want to change: "))
	new_mac=str(input("[*] Enter the new Mac Address: "))
	before=subprocess.check_output(["ifconfig",interface])
	change_mac(interface,new_mac)
	after=subprocess.check_output(["ifconfig",interface])
	if before==after:
		print("[-] Process Failed")
	else:
		print("[+] Success")

main()
