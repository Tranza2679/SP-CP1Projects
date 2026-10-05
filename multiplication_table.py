# Santiago Pineda, Multiplication table
import time
x = 1
print("Welcome to multiplication table!")
while True:
    try:
        number_to_multiply = int(input("What number do you want it to be multplied to at most? "))
    except:
        print("Please write a whole number")
    else:
        break
while number_to_multiply >= 50:
    print("Hey that's way too large of a number, it should be below 50 please")
    while True:
        try:
            number_to_multiply = int(input("What number do you want it to be multplied to at most? "))
        except:
            print("Please write a whole number")
        else:
            break
if number_to_multiply >= 20:
    print("That's going to take forever for all of it to print out, but you chose this. Have fun!")
print(f"The number being used is {x}")
while True:
    for i in range(1,number_to_multiply):
        print(i * x)
        time.sleep(.5)
    x += 1
    if x <= 12:
        print(f"The number being used is {x}")
    else:
        break