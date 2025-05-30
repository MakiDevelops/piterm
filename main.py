import os
import time

# Set vars
commands = ["apl","time","help","exit"]
name = "PiTerm"
version = 1
defvar = "var"
im = ">>"
notexts = ["Hello? Do you see my Mama?", "Can't a man giggle these days?"]
helptext = commands
# Console Boot

print(f"{name} {version}")

# Console Loop
while True:
    a = input(im)
    if a in commands:
        if a in notexts:
            print("No.")
        if a == "apl":
           import apl
        if a == "help":
            print(helptext)
    else:
        print("That command does not exist.")
    
