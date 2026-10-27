#Santiago Pineda, Password strength checker
program_continue = True


special_characters = ["!", "@", "(", ")", "#", "$", "%", "&", "^", "*", "_", "-", "+", "=", "[", "]", "{", "}", "|", "?", "<", ">"] #(!@#$%^&*()_+-=[]{}|;:,.<>?

def checker_for_special(check):
    global special_characters
    if special_characters in check:
        return True
    else:
        pass

print("Welcome to password strength checker! This program checks if a password is actually strong or weak, or maybe even just okay.")
print(f"Note that if you do include special characters in your password(Which you should...), then this is the special characters you CAN use: \n{special_characters}")

while program_continue == True:
    points = 0
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
    list_password = fixed_password.split()
    password_length = len(list_password)
    checker_for_special(list_password)
    if True:
        points =+ 1
    if len(fixed_password) > 8:
        points =+ 1
    for i in range(1, password_length):
        print("Yo free lunacy")
    
    
    
    


    """"first_name = input("What is your first name: ").strip().title()
last_name = input("What is your last name: ").strip().title()
first_seperated_name = first_name.split()
first_fixed = "".join(first_seperated_name)
last_seperated = last_name.split()
last_fixed = "".join(last_seperated)
full_name = first_fixed.title() + " " + last_fixed.title()
print("Hello " +full_name.title())"""