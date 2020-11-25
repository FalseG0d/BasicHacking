import os
import socket

s=socket.socket()
port=8080

host=input(str("[*] Please Enter The Server Address: "))
s.connect((host,port))

print("\n[*] Connected To Server Successfully")
print("")

while 1:
    command=s.recv(1024)
    command=command.decode()

    print("[*] Command Recieved")

    if command=="view_cwd":
        files=os.getcwd()
        files=str(files)
        s.send(files.encode())
        print("[*] Command Executed Successfully")

    else:
        print("[*] Command Output Not Found")