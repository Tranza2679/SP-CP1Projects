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


dice_roll = random.randint(1, dice)
print(f"You got {dice_roll} from your D{dice}")