#Santiago Pineda, combat program
action = 0
def user_combat():
    while True:
        action = int(input("What will you perform? \n 1. attack \n 2. special skill \n 3. defense \n 4. heal"))
        if action > 4:
            print("You really can't do that...")
print("Welcome to the City! Not so much the greatest place to be, especially since you're in the backstreets... Welp, you got it!")
user_name = str(input("What is your name:"))
while True:
    try:
        faction = int(input("What will be your faction? \n 1. The Liu Association(Specializes in melee combat with fire) \n 2. The Middle(Specializes in melee combat and countering after attacks) \n 3. The Thumb(Specializes in long range damage with firearms) \n 4. The Shi Association(Specializes at dealing more damage at low health) \n Please write your choice as the number associated with it!"))
        if faction > 4:
            print("That's not a possible option...")
            continue
    except:
        print("Hey you really can't do that...")
    else:
        break
print("Anyways basic mechanics explanation! \n 1 will cause you to attack with a random skill. \n 2. Will allow you to use a special skil(Most of them will need you to meet some requirement). \n 3. Will cause you to use your defensive action. \n 4. will cause you to heal(note heal lowers with every usage so remember that!)")
if faction == 1:
    print("You are a fixer of the Liu Association! Your stats are: \n Health: 50 \n defense: 4 \n attack: 5")
elif faction == 2:
    print("You are a member of The Middle! Your stats are: \n Health: 60 \n defense: 6 \n attack: 4 ")
elif faction == 3:
    print("You are a member of The Thumb! Your stats are: \n Health: 45 \n defense: 2 \n attack: 7")
elif faction == 4:
    print("You are a fixer of the Shi Association! Your stats are: \n Health: 70 \n defense: 1 \n attack: 4")