#server.py
#run this first 

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('127.0.0.1', 12345))

sock.listen(1)

connections = []

def handler (c, a):
    while True:
        data = c.recv(4098)
        for connection in connections:
            if connection != c:
                  connection.send(data)
        if not data:
              break

while True:
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)

