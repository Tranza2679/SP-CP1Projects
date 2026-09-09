# Santiago Pineda, Idiot proof
first_name = str(input("Please write your first name: ").title().strip())
last_name = str(input("Please write your last name: ").title().strip())
while True:
    try:
        phone_num = int(input("Please write your phone number: "))
    except:
        print("That isn't an actual phone number you know?")
    else:
        break
while True:
    try:
        gpa = float(input('Please write your GPA: '))
    except:
        print("Please write an actual GPA.")
    else: 
        break

first_seperated_name = first_name.split()
first_fixed = "".join(first_seperated_name)
last_seperated = last_name.split()
last_fixed = "".join(last_seperated)
full_name = first_fixed.title() + " " + last_fixed.title()
print("Hello " +full_name.title())

string_phone_num = str(phone_num)
first_part = string_phone_num[0:3]
second_part = string_phone_num[4:7]
third_part = string_phone_num[7:13]
full_phone_num = first_part + " " + second_part + " " + third_part

print(first_part)
print(second_part)
print(third_part)
print(full_phone_num)



