# Santiago Pineda, Factorial calculator
import math

number_list = []
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
number_list.append(number)
full_factorial = math(map(math.factorial, number_list))
print(*list(f"{full_factorial}"))
"""factorials = []
factorial_number = str(math.factorial(number))
def addToList(lists):
    lists.append((factorial_number))
print(factorial_number)

full_answer = addToList(factorials)"""
