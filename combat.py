#Santiago Pineda, combat program
import random
def user_combat(stat_one, max,  stat_two, stat_three, special_ability, enemy_health, enemy_defense, user_count):
    global attack
    global negative_effect
    global ammo
    while True:
        try:
            action = int(input("What will you perform? \n 1. attack \n 2. special skill \n 3. defense \n 4. heal"))
            if action > 4:
                print("You really can't do that...")
        except: 
            print("Please write it as the number associated with it!")
        else:
            break
    if action == 1:
        print("You use your turn to attack the enemy.")
        attack = (random.randint(1, 10) + stat_two)
        enemy_health -= (attack - enemy_defense)
        if special_ability == 1:
            print("You hit the enemy with a burning punch!")
            negative_effect += random.randint(1,5)
            print(f"The enemy has {negative_effect} burn on them!")
        elif special_ability == 2:
            print("You punch the enemy hard before kicking them")
        elif special_ability == 3:
            print("You slash at the enemy with your bayonet on the rifle!")
            if ammo < 2:
                ammo += 1
                print(f"You gain 1 ammo! You now have {ammo} ammo! If at two then you can use your special skill!")
            else:
                print("You have 2 ammo! you can use your special skill")
        else:
            print("You slash at the enemy with a katana! but injure yourself slightly in the process...")
            if stat_one <= 10:
                print("Well you only slighly scratch yourself somehow... so seems you don't take any damage")
            else:
                stat_one -= random.randint(1,3)
            print(f"Your current health is {stat_one}")
            return stat_one
    elif action == 2:
        if user_count >= 5 or ammo == 2:
            print("You do your special skill!")
            if special_ability == 1:
                print("You rush down the enemy and hit them with a burning flying kick!")
                attack = (random.randint(10, 20) + stat_two)
                print(f"You deal {attack} damage to the target!")
                negative_effect +=  random.randint(5,10)
                print(f"The enemy has {negative_effect} burn on them!")
            elif special_ability == 2:
                print("You tackle the enemy and hit them with multiple blows!")
                attack = (random.randint(10,25) + stat_two)
            elif special_ability == 3:
                print("You fire all your ammo into the enemy! ")



print("Welcome to the City! Not so much the greatest place to be, especially since you're in the backstreets... Welp, you got it!")
user_name = str(input("What is your name:"))
while True:
    try:
        faction = int(input("What will be your faction? \n 1. The Liu Association(Specializes in melee combat with fire) \n 2. The Middle(Specializes in melee combat and countering after attacks) \n 3. The Thumb(Specializes in long range damage with rifles) \n 4. The Shi Association(Specializes at dealing more damage at low health) \n Please write your choice as the number associated with it!"))
        if faction > 4:
            print("That's not a possible option...")
            continue
    except:
        print("Hey you really can't do that...")
    else:
        break
print("Anyways basic mechanics explanation! \n 1 will cause you to attack with a random skill. \n 2. Will allow you to use a special skil(Most of them will need you to meet some requirement). \n 3. Will cause you to use your defensive action. \n 4. will cause you to heal(note heal lowers with every usage so remember that!)")
if faction == 1:
    print("You are a fixer of the Liu Association! Your stats are: \n Health: 55 \n defense: 4 \n attack: 5")
    print("Do note all of your attacks inflict burn and cause enemies to take damage after their turn!")
    health = 50
    defense = 4
    attack = 5
    enconter_start = random.randint(1,2)
    if enconter_start == 1:
        print("As you are walking around, you find an unspecting Rat that has been messing with  and ambush them! You start first")
elif faction == 2:
    print("You are a member of The Middle! Your stats are: \n Health: 60 \n defense: 6 \n attack: 4 ")
    print("Do note that after using your counter or getting hit three times. your counter is replaced by your special skill!")
    health = 60
    defense = 6
    attack = 4
elif faction == 3:
    print("You are a member of The Thumb! Your stats are: \n Health: 50 \n defense: 2 \n attack: 7")
    print("Do note that after attacking two times, you'll be able to do your special skill immediately!")
    health = 50
    defense = 2
    attack =7
elif faction == 4:
    print("You are a fixer of the Shi Association! Your stats are: \n Health: 70 \n defense: 1 \n attack: 4")
    print("Do note you lose some health every time you attack... but get stronger at low health")