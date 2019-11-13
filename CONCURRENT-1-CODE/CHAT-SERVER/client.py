#client.py
#run multiple instances of this after starting the server

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 12345))

def sendMsg():
    while True:
        msg = input().encode()
        sock.send(msg)

iThread = threading.Thread(target=sendMsg)
iThread.daemon = True
iThread.start()

while True:
    #this is data received back from the server
    data = sock.recv(4098).decode()
    if not data:
        break
    print(data)
    
