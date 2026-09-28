#Santiago Pineda, What is my grade
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
    
