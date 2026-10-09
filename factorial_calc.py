# Santiago Pineda, Factorial calculator
import math

print("Welcome to factorial calc(short for calculator)")
while True:
    while True:
        try:
            number = int(input("What number do you want to find the factorial for? "))
            if number < 0:
                print("That's below zero, please try again.")
                continue
            break
        except:
            print("Please write a whole number")
        else:
            break
    def factorialize(num):
        return math.factorial(num)

    full_factorial = list(map(factorialize, [number]))
    fixed_factorial = list(full_factorial)[0]
    print((f"{number}! = {fixed_factorial}"))

    user_input = str(input("Do you want to continue using the factorial calculator? Yes or No ")).strip().title()
    if user_input == "Yes":
        print("Okie Doki!")
        continue
    elif user_input == "No":
        print("Alright:(")
        break
    else:
        print("I'll just take that as a no...")
        break
