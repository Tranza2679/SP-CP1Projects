#Santiago Pineda, Password strength checker
program_continue = True
points = 0


special_characters = ["!", "@", "(", ")", "#", "$", "%", "&", "^", "*", "_", "-", "+", "=", "[", "]", "{", "}", "|", "?", "<", ">"] #(!@#$%^&*()_+-=[]{}|;:,.<>?

def checker_for_special(check):
    global special_characters
    if special_characters in check:
        return True
    else:
        pass



def pointIncreasor(first_time):
    global points
    if first_time:
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
    checker_for_special(list_password)
    if True:
        print("chud")
        pointIncreasor(False)
    
    if password_length >= 8:
        print("poop")
        pointIncreasor(False)

    
    
    print(f"{points}")
    
    
    