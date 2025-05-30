from time import sleep

number = 3.14159265359
print("Calculating PI *2")
print("!WARNING, MAY LAG!")
print("ENTER to start")
input()
while True:
    sleep(0.01)
    number *= 2
    print(number)
    if number == float('inf'):
        number = 3.14159265359
            
        