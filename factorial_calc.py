# Santiago Pineda, Factorial calculator
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
for i in range(1,number, -1):
    factorial_number = number * i 
    print(f"")
