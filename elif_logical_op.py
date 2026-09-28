# Santiago Pineda, elif and logical operators notes

age = 15
license = True

if age >= 18:
    print("You are an adult and can vote!")
elif age >= 15 and license:
    print("You can drive ! stil go to school.")
elif age >= 15 and not license:
    print("You could drive...but you haven't done the paperwork:((( Also go to school!")
else:
    print("You are too young to drive, so go to school!")

win = True
hp = 25

if win or hp <= 0:
    print("Game is over, poo") #Pass is a placeholder! pretty fun fact!
    if hp > 0:
        pass
    else:
        print("You lost:(")
else:
    print("The game is still going")