from time import sleep
import os
import random

#vars
hp = 3
dmg = 1
gc = "y"
bc = "n"
setname = "A man runs up to you. He askes your name. What is it?"
rand = "You find a rock on the ground. Do you take it?"
bad = ['It was poisoned!',"It didn't even exist?"]
badend = f"You took {dmg}!"

#game
print("I Don't Know: A Game")
print("Press ENTER to play!")
input()
print(setname)
playername = input(">>")
print(f"Man: Ah! Your name is {playername}")
sleep(2)
print("Man: From now on, everything will be random.")
sleep(2)
print("Man: Good luck!")
sleep(2)
os.system('clear')
sleep(1)
print(rand)
a = input("y/n >>")
if a == "y":
    print(bad)
    dmg = 1
    print(badend)