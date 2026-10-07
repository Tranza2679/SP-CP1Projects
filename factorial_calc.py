# Santiago Pineda, Factorial calculator
import math


print("Welcome to factorial calc(short for calculator)")
while True:
    try:
        number = int(input("What number do you want to find the factorial for? "))
    except:
        print("Please write a whole number")
    else:
        break
while number < 0:
    print("Please write something else")
    while True:
        try:
            number = int(input("What number do you want to find the factorial for? "))
        except:
            print("Please write a whole number")
        else:
            break

full_answer = map(int, math.factorial, number)
print(*list(full_answer))