# Santiago Pineda, User Sign in

user = "ImSoBeautiful29"
password = "DirtlooksNiCe24"

user_input = input("What is the username you are using: ")
password_input = input("What is the password for that account: ")

if user_input == user and password_input == password: 
    print("You were able to correctly sign in! The user and password are correct!")
elif user_input == user or password_input == password:
    if user_input == user:
        print("You got he user")