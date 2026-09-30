#SP programming 1, What is my grade
continue_program = True
while continue_program:
    while True:
        try:
            grade = float(input('What is your grade? '))
        except:
            print("Please write an actual grade:(")
        else:
            break
    if grade >= 97:
        print("Wow, you got an A+! Great job you know?")
    elif grade >= 94:
        print("You got an A! That's pretty nice!")
    elif grade >= 90:
        print("You got an A- which is still pretty fine!")
    elif grade >= 87:
        print("Nice, you got a B+")
    elif grade >= 84:
        print("Alright, you got a B")
    elif grade >= 80:
        print("Okay, you got a B-")
    elif grade >= 77:
        print("You have a C+, could be better")
    elif grade >= 74:
        print("You have a C, there's room to improve but it's fine.")
    elif grade >= 70:
        print("You have a C-, definetely could improve")
    elif grade >= 67:
        print("You have a D+, you could improve your grade")
    elif grade >= 64:
        print("You have a D, please lock in")
    elif grade >= 60:
        print("You have a D-, uh oh:(")
    elif grade >= 57:
        print("Goodness you have a F+, yikes")
    elif grade >= 54:
        print("You just have an F! :((((")
    else:
        print("You have a F-! Big yikes!")
    while True:
        try:
            user_continue = str(input("Would you like to continue? Yes or No ")).strip().title()
        except:
            print("Please write an actual response:(")
        else:
            break
    continue_program = True if user_continue == "Yes" else False
