import os
import subprocess

# vars
dir_path = os.path.dirname(os.path.realpath(__file__))
# term
print("appLoader")
print(dir_path)
while True:
    a = input(">>")
    if a == "pi":
        subprocess.run(["python3", "loaded_apps/pi2.py"])
    if a == "idk":
        subprocess.run(["python3", "loaded_apps/idk.py"])