#Santiago Pineda, Flexible Calculator
#Make calculator function
#Max goes through the numbers and changes it if it is higher than the last number
#Min does the opposite 
max_num = 0
number_list = []
total = 0
min_num = 0
product_num = 0
num = 0
final_num = 0 
def sum(*args):
    global total 
    for num in args:
        total += num
    return total

def average(*args):
    global total
    for num in args:
        total += num
        i += 1
    total /= i 
    return total

def max(*args):
    global max_num
    for num in args:
        if max_num < num:
            max_num = num
        else:
            pass
    return max_num

def min(*args):
    global min_num 
    min_num = args[0]
    for num in args:
        if min_num > num:
            min_num = num
        else:
            pass
    return min_num

def product(*args):
    global product_num
    product_num = args[0]
    for num in args:
        product_num *= num
    return product_num

def getNum():
    global number_list
    global num
    while True:
        try:
            num = input("Number: ") 
            if isinstance(num, int):
                number_list.append(num)
            elif isinstance(num, str):
                if num == "done":
                    break
                else:
                    print("Please write done or an actual number")
                    continue
            else:
                continue
        except:
            print("Please write done or an actual number")
        else:
            break
    return number_list

def calc(op, *args):
    global final_num
    if op == "sum":
        final_num = sum(*args)
        print(f"Result: {final_num}")
    elif op == "average":
        final_num = average(*args)
        print(f"Result: {final_num}")
    elif op == "max":
        final_num = max(*args)
        print(f"Result: {final_num}")
    elif op == "min":
        final_num = min(*args)
        print(f"Result: {final_num}")
    elif op == "product":
        final_num = product(*args)
        print(f"Result: {final_num}")

print("Hello! Welcome to Flexible Calculator!")
print("Available operaions: sum, average, max, min, product.")
while True:
    while True:
        try:
            operation = str(input("What opteration will you perform: ")).lower()
            if operation != "sum" and operation != "average" and operation != "max" and operation != "min" and operation != "product":
                print('That is not an available operation:( Please try again.')
                continue
        except:
            print("Please try again.")
        else:
            break
    number_list = getNum()
    if operation == "sum":
        print(*f"Calculating sum of {number_list}")
        calc(operation, number_list)
    elif operation == "average":
        print(*f"Calculating average of {number_list}")
        calc(operation, number_list)
    elif operation == "max":
        print(*f"Calculating maximum of {number_list}")
        calc(operation, number_list)
    elif operation == "min":
        print(*f"Calculating mininum of {number_list}")
        calc(operation, number_list)
    elif operation == "product":
        print(*f"Calculating product of {number_list}")
        calc(operation, number_list)
    else:
        print("I have no idea how this happened, but if it did, then beats me.")
        break
    number_list = []
    while True:
        try:
            user_input = str(input("Do you want to continue with this program: ")).lower().strip()
            if user_input != "yes" or user_input != "no":
                print("Please write yes or no.")
                continue
        except:
            print("Please write it again")
        else:
            break

    if user_input == "yes":
        print("Thank you for continuing.")
        pass
    else:
        print("Thank you for using this calculator")
        break

