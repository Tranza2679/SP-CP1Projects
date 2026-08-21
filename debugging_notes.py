# Santiago Pineda Debugging notes

#Syntax error 
"""print("hello)

#indentation error
if True:
print("This is True")

people = 10
print(people)""" 

#logic error
#Read the code again
apples = 20
people = 3

print(apples / people)

# Run-Time Errors
while True:
    try:
        fav_num = int(input("What is your favorite number: "))
    except: 
        print("That's not a number!")
    else: 
        break 

print(4 + fav_num)