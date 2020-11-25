import os
import socket

s=socket.socket()
host=socket.gethostname()

port=8080
s.bind((host,port))
print("\n[*] Server Is Currently Runninng @",host)
print("\nWaiting For Incoming Connections....")
s.listen(1)

con,addr=s.accept()

print(addr, " has connected to the server successfully ")

while 1:
    command=input(str("Command >> "))

    if command=="view_cwd":
        con.send(command.encode())
        print("[*] Command Waiting For Execution")
        print("[*] Command Executed")

        files=con.recv(1024)
        files=files.decode()

        print("[*] Command Output : ",files)

    else:
        print("[*] Command Output Not Found")