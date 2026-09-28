# Santiago Pineda, User Sign in

user = "ImSoBeautiful29"
password = "DirtlooksNiCe24"

while True:
    try:
        user_input = str(input("What is the username you are using: "))
        password_input = str(input("What is the password for that account: "))
    except:
        print("Please write it again:(")
    else:
        break
check_user = True if user_input == user else False
check_password = True if password_input == password else False
if check_user and check_password:
    print("You were able to correctly sign in! The user and password are correct!")
    print(f"Welcome back {user}!")
elif check_user and not check_password:
    print("You got the user correct but not the password")
elif check_password and not check_user:
        print("You got the password correct but not the user")
else:
     print("You got both the password and user wrong, get out of here!")