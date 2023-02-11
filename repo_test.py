import subprocess

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "--all"])
subprocess.call(["git", "add", "README.md"])
subprocess.call(["git", "commit", "-m", "test"])
#subprocess.call(["git", "push"])