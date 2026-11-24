#Santiago Pineda, Flexible Calculator
#Make calculator function
#Max goes through the numbers and changes it if it is higher than the last number
#Min does the opposite 
def calc_sum(*args): #FINDS the sum of a list by adding every number in that list individually before returning the final number.
    total = 0
    for num in args:
        total += num
    return total

def calc_average(*args): #FINDS the average of all numbers in a list that is given to it, works the same as a sum besides it having i increase for every number added before dividing the total by i to find the average 
    i = 0
    total = 0
    for num in args:
        total += num
        i += 1
    total /= i 
    return total

def calc_max(*args): #FINDS the maximum of a list given to it, and loops through every number seeing if its larger than the last number given. Starts as the first number given
    max_num = args[0]
    for num in args:
        if max_num < num:
            max_num = num
        else:
            pass
    return max_num

def calc_min(*args): #FINDS the mininum number of a list given to it, and loops through every number seeing if there a smaller number and returns the smallest value.
    min_num = args[0] #SET to the first number in the list of numbers given
    for num in args:
        if min_num > num:
            min_num = num
        else:
            pass
    return min_num

def calc_product(*args): #FINDS the product of all numbers given to it, and returns the final number
    product_num = 1 #Set to 1 just so it has no noticeable effect 
    for num in args:
        product_num = product_num * num 
    return product_num

def getNum(): #Meant to get the number the user wants, and if they put done then it stops. If they put something that isn't done, then it prints an error message and repeats
    number_list = []
    while True:
        num = input("Number: ").lower().strip()
        if num == "done":
            break
        else:
            try:
                number_list.append(float(num))
            except ValueError:
                print("Please write a number or done")
    return number_list

def calc(op, *args): #The main calculator for the program, just acts as a way to get the specific result and display it for the list and operation given to us
    if op == "sum":
        final_num = calc_sum(*args)
    elif op == "average":
        final_num = calc_average(*args)
    elif op == "max":
        final_num = calc_max(*args)
    elif op == "min":
        final_num = calc_min(*args)
    elif op == "product":
        final_num = calc_product(*args)

    print(f"Result: {final_num}")
    return final_num

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
    number_list= getNum()
    while True:
        if len(number_list) == 0:
            print("Please write something!!!!")
            number_list = getNum()
        else:
            break

    if operation == "sum":
        print("Calculating sum of", *number_list)
        calc(operation, *number_list)
    elif operation == "average":
        print("Calculating average of", *number_list)      
        calc(operation, *number_list)
    elif operation == "max":
        print("Calculating maximum of", *number_list)
        calc(operation, *number_list)
    elif operation == "min":
        print("Calculating mininum of", *number_list)
        calc(operation, *number_list)
    elif operation == "product":
        print("Calculating product of", *number_list)
        calc(operation, *number_list)
    else:
        print("I have no idea how this happened, but if it did, then beats me.")
        break
    number_list = []
    while True:
        try:
            user_input = str(input("Do you want to continue with this program: ")).lower().strip()
            if user_input != "yes" and user_input != "no":
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

