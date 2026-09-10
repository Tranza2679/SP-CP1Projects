# SP, dice roller
import random
print("Hello, welcome to dice roller")
print("The options of dice you have include: D4, D6, D8, D10, D12, D20")
dice = 1
while True:
    try:
        dice = int(input("Please write how much sides the dice you want has: "))
        if dice % 2 == 1:
            print("Please note your dice should be even sided!")
            choice = "bad"
            while choice == "bad":
                try: 
                    dice = int(input("Please write how much sides the dice you want has: "))
                except:
                    print("Please just write it as an even sided dice")
                else:
                    choice = "good"
        elif dice > 20:
            print("That's way too big of a dice for this!")
            choice = "bad"
            while choice == "bad":
                try: 
                    dice = int(input("Please write how much sides the dice you want has: "))
                except:
                    print("Please just write it less than 20")
                else:
                    choice = "good"
        else:
            print("I love your choice!")
    except:
       print("Please write an actual dice!!!!")
    else:
        break

dice_roll = random.randint(1, dice)
print(f"You got {dice_roll} from your D{dice}")