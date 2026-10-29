#Santiago Pineda, Password strength checker
program_continue = True
points = 0
special_characters_yes = False

password_list = []


special_characters = ["!", "@", "(", ")", "#", "$", "%", "&", "^", "*", "_", "-", "+", "=", "[", "]", "{", "}", "|", "?", "<", ">"] #(!@#$%^&*()_+-=[]{}|;:,.<>?

def checker_for_special(checker,checks):
    global special_characters_yes
    if checker in checks:
        special_characters_yes = True
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
    Checker_for_number = False
    print(checker_for_special(special_characters,list_password))
    
    if True:
        print("chud")
        pointIncreasor(False)
    
    if password_length >= 8:
        print("poop")
        pointIncreasor(False)
    checker_for_upper = True if list_password.isupper() else False
    if checker_for_upper == True:
        print("Dih")
        pointIncreasor(False)
    checker_for_lower = True if fixed_password.islower() else False
    if checker_for_lower == True:
        print("Bleh")
        pointIncreasor(False)
    Checker_for_number = True if fixed_password.isnumeric() else False
    if Checker_for_number == True:
        print("oops")
        pointIncreasor(False)

    if points == 5 or points == 4:
        print(f"Your password: {fixed_password}, is strong! Good job!")
    elif points == 3:
        print(f"Your password: {fixed_password}, is okay. You can do better")
    else:
        print(f"Your password: {fixed_password}, is weak. Please consider adding some changes to it")
    while True:
        try:
            continue_or_not = str(input("Will you continue? Yes or No")).strip().title()
            if continue_or_not != "Yes" or continue_or_not != "No":
                print("You can't do that, please write it again")
                pass
        except:
            print("You can't write that!")


    
    
    print(f"{points}")
    
    
    