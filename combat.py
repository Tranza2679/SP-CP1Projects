#Santiago Pineda, combat program
import random
heal = 30
enemy_heal = 30
enemy_guard = False
defense = False 
bad_attack = False
bad_enemy_attack = False
special_counter = 0
counter = False
negative_effect = 0
def userCombat(stat_one, max,  stat_two, special_ability, enemy_health, enemy_defense, user_count):
    global attack
    global negative_effect
    global ammo
    global counter 
    global defense
    global heal
    global change
    global enemy_guard
    while True:
        try:
            print("What will you perform? \n 1. attack \n 2. special skill \n 3. defense \n 4. heal")
            action = int(input(""))
            if action > 4:
                print("You really can't do that...")
        except: 
            print("Please write it as the number associated with it!")
        else:
            break
    if action == 1:
        print("You use your turn to attack the enemy.")
        
        if enemy_guard == True:
            attack = (random.randint(1, 10) + stat_two - (enemy_defense * 2))
            enemy_guard = False
        else:
            attack = (random.randint(1, 10) + stat_two - enemy_defense)

        if attack <= 0:
            print("The attack somehow deals 0 damage...")
        else:
            enemy_health -= attack
            print(f"The enemy currently has {enemy_health} health")
             

        if special_ability == 1:
            print("You hit the enemy with a burning punch!")
            negative_effect += random.randint(1,3)
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
            if stat_one <= 30:
                print("Well you only slighly scratch yourself somehow... so seems you don't take any damage. You also do extra damage out of despiration")
                attack += stat_two
                enemy_health -= (attack - enemy_defense)
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
                enemy_health -= attack
                print(f"You deal {attack} damage to the target!")
                negative_effect +=  random.randint(5,10)
                print(f"The enemy has {negative_effect} burn on them!")
                 
            elif special_ability == 2:
                print("You tackle the enemy and hit them with multiple blows!")
                attack = (random.randint(10,25) + stat_two)
                enemy_health -= attack
                
            elif special_ability == 3:
                print("You fire all your ammo into the enemy! ")
                attack = (random.randint(15,25) + stat_two)
                enemy_health -= attack
                
            elif special_ability == 4:
                print("You harness all your strength to do a powerful slash!")
                attack = random.randint(1,4)
                if attack == 4:
                    print("You hit the lucky four and get + 45 to the damage")
                    attack += 45
                    enemy_health -= attack
                    
                else:
                    print("Sadly you fail so your attack doesn't deal too much damage...")
                    enemy_health -= attack
                    
            else:
                print("You are unable to use your special skill...")
                while True:
                    try:
                        action = int(input("What will you perform? \n 1. attack \n 2. special skill \n 3. defense \n 4. heal"))
                        if action > 4:
                            print("You really can't do that...")
                    except: 
                        print("Please write it as the number associated with it!")
                    else:
                        break
    elif action == 3:
        print("You block! the next hit you take will take reduced damage by your defense X 2")
        defense = True
        if special_ability == 2:
            counter = True
    elif action == 4:
        print("You use your turn to recover some health!")
        if heal <= 0:
            print("You can't heal an effective amount... maybe do something else?")
            while True:
                try:
                    action = int(input("What will you perform? \n 1. attack \n 2. special skill \n 3. defense \n 4. heal"))
                    if action > 4:
                        print("You really can't do that...")
                except: 
                    print("Please write it as the number associated with it!")
                else:
                    break
        else:
            stat_two += heal
            if stat_two > max:
                change = stat_two - max
                stat_two -= change 
            heal -= 7
            print(f"Your heal will now only recover {heal} amount...")
    return enemy_health and stat_two
    
def enemyCombat( enemy_stat_one, enemy_health, user_defense, user_health, enemy_count, enemy_max, user_attack ):
    global enemy_guard 
    global defense
    global enemy_heal
    global change
    global bad_enemy_attack
    global special_counter
    action = random.randint(1,4)
    if action == 1:
        print("The Rat hits you with a bat!")
        if defense == True:
            attack =(random.randint(1, 15) + enemy_stat_one - (user_defense * 2))
            defense = False
        else:
            attack = (random.randint(1, 15) + enemy_stat_one - user_defense)
        
        if attack < 0:
            print("Somehow it deals 0 damage")
            bad_enemy_attack = True
        else:
            user_health -= attack
            print(f"You now only have {health} ")

        if counter == True and bad_enemy_attack == False:
            if special_counter >= 3:
                print("As you get hit, you use your special counter and attack.")
                print("You tackle the enemy and hit them with multiple blows!")
                attack = (random.randint(10,25) + user_attack)
                enemy_health -= attack
                special_counter = 0
            else:
                print("As you get hit, you counter back")
                attack = (random.randint(1, 6) + user_attack)
                enemy_health -= attack
                special_counter += 1
        elif bad_enemy_attack == False:
            user_health -= (attack)
        else:
            bad_enemy_attack = False
            
    elif action == 2:
        if enemy_count == 5:
            print("The Rat does their special attack and hits you with a strong slam of their bat!")
            attack = (random.randint(10,20) + enemy_stat_one)
            user_health -= attack
            print(f"You now have {user_health} health")
        else:
            action = random.randint(1,4)
    elif action == 3:
        print("The Rat takes a guarding stance, they take their defense X 2 less damage for the next attack")
        enemy_guard = True 
    elif action == 4: 
        print("The Rat heals their wound")
        if enemy_heal <= 0:
            print("The enemy realizes that maybe it can't heal so they change their action.")
            action = random.randint(1,4)
        else:
            enemy_health += enemy_heal
            if enemy_health > enemy_max:
                change = enemy_health - enemy_max
                enemy_health -= change
            enemy_heal -= 7
            print(f'The enemy will now only recover {enemy_heal} amount with their heal.')
    return user_health and enemy_health

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
    health = 55
    defense = 4
    attack = 5
    max_health = 55
    health_enemy = 70
    max_enemy = 70
    defense_enemy = 4
    attack_enemy = 6
    special_count = 0
    enemy_special_count = 0
    enconter_start = random.randint(1,2)
    if enconter_start == 1:
        print("As you are walking around, you find an unspecting Rat that has been messing with people around and ambush them! You start first!")
        while health >= 0 or health_enemy >= 0:
            userCombat(health, max_health, attack, faction, health_enemy, defense, special_count)
            special_count += 1
            enemyCombat(attack_enemy, health_enemy, defense, health, enemy_special_count, max_enemy, attack)
            enemy_special_count += 1
            if negative_effect > 0:
                print(f"The enemy takes {negative_effect} damage")
                health_enemy -= negative_effect
    else:
        print("As you are walking around, you get ambushed by a Rat! The enemy starts first.")
        while health >= 0 or health_enemy >= 0:
            enemyCombat(attack_enemy, health_enemy, defense, health, enemy_special_count, max_enemy, attack)
            enemy_special_count += 1
            if negative_effect > 0:
                print(f"The enemy takes {negative_effect} damage")
                health_enemy -= negative_effect
            userCombat(health, max_health, attack, faction, health_enemy, defense, special_count)
            special_count += 1

    if health <= 0:
        print("You lose:/ ")
    elif health_enemy <= 0:
        print('You win!!!')
elif faction == 2:
    print("You are a member of The Middle! Your stats are: \n Health: 60 \n defense: 6 \n attack: 4 ")
    print("Do note that after using your counter or getting hit three times. your counter is replaced by your special skill!")
    health = 60
    defense = 6
    attack = 4
    max_health = 60
    health_enemy = 70
    max_enemy = 70
    defense_enemy = 4
    attack_enemy = 6
    special_count = 0
    enemy_special_count = 0
    enconter_start = random.randint(1,2)
    if enconter_start == 1:
        print("As you are walking around, you find an unspecting Rat that has been messing with people around and ambush them! You start first!")
        while health >= 0 or health_enemy >= 0:
            userCombat(health, max_health, attack, faction, health_enemy, defense, special_count)
            special_count += 1
            enemyCombat(attack_enemy, health_enemy, defense, health, enemy_special_count, max_enemy, attack)
            enemy_special_count += 1
    else:
        print("As you are walking around, you get ambushed by a Rat! The enemy starts first.")
        while health >= 0 or health_enemy >= 0:
            enemyCombat(attack_enemy, health_enemy, defense, health, enemy_special_count, max_enemy, attack)
            enemy_special_count += 1
            userCombat(health, max_health, attack, faction, health_enemy, defense, special_count)
            special_count += 1
    
        if health <= 0:
            print("You lose:/ ")
        elif health_enemy <= 0:
            print('You win!!!')
elif faction == 3:
    print("You are a member of The Thumb! Your stats are: \n Health: 50 \n defense: 2 \n attack: 7")
    print("Do note that after attacking two times, you'll be able to do your special skill immediately!")
    health = 50
    defense = 2
    attack =7
    max_health = 50
    health_enemy = 70
    max_enemy = 70
    defense_enemy = 4
    attack_enemy = 6
    special_count = 0
    enemy_special_count = 0
    enconter_start = random.randint(1,2)
    if enconter_start == 1:
        print("As you are walking around, you find an unspecting Rat that has been messing with people around and ambush them! You start first!")
        while health >= 0 or health_enemy >= 0:
            userCombat(health, max_health, attack, faction, health_enemy, defense, special_count)
            special_count += 1
            enemyCombat(attack_enemy, health_enemy, defense, health, enemy_special_count, max_enemy, attack)
            enemy_special_count += 1
    else:
        print("As you are walking around, you get ambushed by a Rat! The enemy starts first.")
        while health >= 0 or health_enemy >= 0:
            enemyCombat(attack_enemy, health_enemy, defense, health, enemy_special_count, max_enemy, attack)
            enemy_special_count += 1
            userCombat(health, max_health, attack, faction, health_enemy, defense, special_count)
            special_count += 1
    
        if health <= 0:
            print("You lose:/ ")
        elif health_enemy <= 0:
            print('You win!!!')
elif faction == 4:
    print("You are a fixer of the Shi Association! Your stats are: \n Health: 70 \n defense: 1 \n attack: 6")
    print("Do note you lose some health every time you attack... but get stronger at low health")
    health = 70
    defense = 1
    attack = 6
    max_health = 70
    health_enemy = 70
    max_enemy = 70
    defense_enemy = 4
    attack_enemy = 6
    special_count = 0
    enemy_special_count = 0
    enconter_start = random.randint(1,2)
    if enconter_start == 1:
        print("As you are walking around, you find an unspecting Rat that has been messing with people around and ambush them! You start first!")
        while health >= 0 or health_enemy >= 0:
            userCombat(health, max_health, attack, faction, health_enemy, defense, special_count)
            special_count += 1
            enemyCombat(attack_enemy, health_enemy, defense, health, enemy_special_count, max_enemy, attack)
            enemy_special_count += 1
    else:
        print("As you are walking around, you get ambushed by a Rat! The enemy starts first.")
        while health >= 0 or health_enemy >= 0:
            enemyCombat(attack_enemy, health_enemy, defense, health, enemy_special_count, max_enemy, attack)
            enemy_special_count += 1
            userCombat(health, max_health, attack, faction, health_enemy, defense, special_count)
            special_count += 1
    
    if health <= 0:
        print("You lose:/ ")
    elif health_enemy <= 0:
        print('You win!!!')