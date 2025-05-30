import os

# vars
dir_path = os.path.dirname(os.path.realpath(__file__))
# term
print("appLoader")
print(dir_path)
a = input(">>")
if a == "pi":
    import pi2
if a == "idk":
    import idk
