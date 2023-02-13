CS361 Microservice

THe goal of this microservice is to assist in github automation by automatically creating and returning a link to a repository.

To request data:
Data is sent/received through sockets. The server.py file contents can be implemented into whichever part of the project uses the microservice.
In order to receive a link to the github repository, first certain data must be passed to the microservice.
The data dictionary in server.py contains the parameters that the repository will be created by, they are hardcoded in purely for example purposes.
The line clientsocket.send(json.dumps(data).encode('utf-8')) sends data to the microservice.

To receive data:
The microservice creates the github repository based on the parameters sent to it, and returns a link.
The line msg = clientsocket.recv(1024).decode('utf-8') receive the message and turns it into a variable that can be operated on however is useful.

UML sequence diagram:
![alt text](https://i.imgur.com/Ue3fMha.png)