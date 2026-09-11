# SP, dice roller
import random
print("Hello, welcome to dice roller")
print("The options of dice you have include: D4, D6, D8, D10, D12, D20")
while True:
    try:
        dice = int(input("Please write how much sides the dice you want has as a whole number: "))
    except:
        print("Please write it as a whole number.")
    else:
        break
while dice % 2 == 1:
    print("A dice really can't be odd you know? It's an odd thing to write!!!!")
    while True:
        try:
            dice = int(input("Please write how much sides the dice you want has as a whole number: "))
        except:
            print("Please write it as a whole number.")
        else:
            break
while dice > 20:
    print("That dice is ummm really big. Maybe write it as one of the options...?")
    while True:
        try:
            dice = int(input("Please write how much sides the dice you want has as a whole number: "))
        except:
            print("Please write it as a whole number.")
        else:
            break
print(f"Great option for a dice! I probably would've picked the same thing as {dice} is my favorite number!")
dice_roll = random.randint(1, dice)
print(f"You got a {dice_roll} from your D{dice}!")
