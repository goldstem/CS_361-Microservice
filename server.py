import socket
import json


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9876
s.bind((socket.gethostname(), port))

s.listen(5)

data = {
    "name": "demo_video",
    "description": "test",
    "private": True
}

while True:
    clientsocket, address = s.accept()
    print("Connected to " + str(address))

    clientsocket.send(json.dumps(data).encode('utf-8'))

    msg = clientsocket.recv(1024).decode('utf-8')
    print(msg)

    clientsocket.close()
