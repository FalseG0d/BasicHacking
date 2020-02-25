#!/usr/bin/python3
#Simple Program to return 3 different types of hash code for the input String

import hashlib

hashValue=input("[*] Enter the hash value: ")

hashObj1=hashlib.md5()
hashObj1.update(hashValue.encode())

hashObj2=hashlib.sha1()
hashObj2.update(hashValue.encode())

hashObj3=hashlib.sha224()
hashObj3.update(hashValue.encode())

hashObj4=hashlib.sha256()
hashObj4.update(hashValue.encode())

hashObj5=hashlib.sha512()
hashObj5.update(hashValue.encode())

print("md5        "+hashObj1.hexdigest())
print("sha1       "+hashObj2.hexdigest())
print("sha224:    "+hashObj3.hexdigest())
print("sha256:    "+hashObj4.hexdigest())
print("sha512:    "+hashObj5.hexdigest())

