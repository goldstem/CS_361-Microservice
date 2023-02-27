import time
import requests
import json
import socket
import secret

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        s.bind(('127.0.0.1', 9876))
        break
    except:
        print("Retrying bind to port 9876...")
        time.sleep(5)
        pass

print("Successfully bound to port 9876")

s.listen(5)

s, address = s.accept()
print("Connected to " + str(address))

msg = s.recv(1024).decode('utf-8')
msg = json.loads(msg)

pat = secret.TOKEN
api = "https://api.github.com"
user = secret.USER
print(msg)

print("Creating repository: " + msg["name"])
response = requests.post(api + "/user/repos", data=json.dumps(msg), headers={"Authorization": "token " + pat})
response.raise_for_status()

repo_link = "https://github.com/" + user + "/" + msg["name"]

if response.status_code == 201:
    new_msg = s.send(("Created repository at: " + repo_link).encode('utf-8'))
else:
    print("Error: repository creation failed")




