#Santiago Pineda, Password strength checker
program_continue = True
points = 0
special_characters_yes = False

password_list = []


special_characters = ["!", "@", "(", ")", "#", "$", "%", "&", "^", "*", "_", "-", "+", "=", "[", "]", "{", "}", "|", "?", "<", ">"] #(!@#$%^&*()_+-=[]{}|;:,.<>?

def checker_for_special(checker,checks):
    global special_characters_yes
    for check in checks:
        if checker in checks:
            special_characters_yes = True
            break
        else: 
            pass 



def pointIncreasor(reset):
    global points
    if reset:
        points = 0
    else:
        points += 1
        return points

print("Welcome to password strength checker! This program checks if a password is actually strong or weak, or maybe even just okay.")
print(f"Note that if you do include special characters in your password(Which you should...), then this is the special characters you CAN use: \n{special_characters}")

while program_continue == True:
    while True:
        try:
            password = str(input("What is the password you want to check? ")).strip()
            if len(password) >= 40:
                print("That password is really long... I'm sure it's good but how will you remember?")
                continue
        except:
            print("Please write again")
        else:
            break
    separated_password = password.split()
    fixed_password = "".join(separated_password)
    list_password = list(fixed_password)
    password_length = len(fixed_password)
    checker_for_upper = False
    checker_for_lower = False
    checker_for_number = False
    for char in list_password:
        if char in special_characters:
            special_characters_yes = True
        else:
            pass
    for letter in list_password:
        if letter.isupper():
            checker_for_upper = True
        elif letter.islower():
            checker_for_lower = True
        elif letter.isnumeric():
            checker_for_number = True
        else:
            pass

    
    
    if special_characters_yes==True:
        print("There are special characters in your password!")
        pointIncreasor(False)
    else:
        print("There is not a special character in your password:(")
    if password_length >= 8:
        print("There is at least 8 characters in your password!")
        pointIncreasor(False)
    else: 
        print("There is not at least 8 characters in your password:(")
    if checker_for_upper == True:
        print("There is at least 1 uppercase letter in your password!")
        pointIncreasor(False)
    else:
        print("There is no uppercase letters in your password:(")
    if checker_for_lower == True:
        pointIncreasor(False)
        print("There is at least 1 lowercase letter in your password!")
    else:
        print("There is no lowercase letter in yoyr password(somehow):(")
    if checker_for_number == True:
        print("There is at least 1 number in your password!")
        pointIncreasor(False)
    else:
        print("There is no number in your password:(")

    if points == 5 or points == 4:
        print(f"Your password: {fixed_password}, is strong! Good job!")
    elif points == 3:
        print(f"Your password: {fixed_password}, is okay. You can do better")
    else:
        print(f"Your password: {fixed_password}, is weak. Please consider adding some changes to it")
    while True:
        try:
            continue_or_not = str(input("Will you continue? Yes or No ")).strip().title()
            if continue_or_not != "Yes" and continue_or_not != "No":
                print("You can't do that, please write it again")
                continue
        except:
            print("You can't write that!")
        else: 
            break
    if continue_or_not == "Yes":
        pointIncreasor(True)
    else:
        break
    