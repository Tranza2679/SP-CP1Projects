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
        num = input("Number: ") 
        if isinstance(num, int):
            number_list.append(num)
        elif isinstance(num, str):
            if num == "done":
                break
            else:
                print("Please write done or an actual number")
    return number_list

def calc(op, *args):
    if op == "sum":
        print("Please write the numbers you want to use! ")

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
