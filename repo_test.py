import requests
import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 9876))

msg = s.recv(1024).decode('utf-8')
msg = json.loads(msg)

print(msg)

pat = "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"
api = "https://api.github.com"
user = "goldstem"

response = requests.post(api + "/user/repos", data=json.dumps(msg), headers={"Authorization": "token " + pat})
response.raise_for_status()

repo_link = "https://github.com/" + user + "/" + msg["name"]

if response.status_code == 201:
    new_msg = s.send(("Created repository at: " + repo_link).encode('utf-8'))
else:
    print("Error: repository creation failed")


