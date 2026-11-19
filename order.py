#Santiago Pineda, Order Up!
import random
import time
waiter_name = ""
waiter_personality = ""
drink = ""
main = ""
side_one = ""
side_two = ""
dessert = ""


menu = {
    "Drinks" : {
        "Lemonade": 2.50,
        "Coke": 2.00,
        "Miller Lite": 5.00,
        "Diet Coke": 2.00,
        "Sprite": 2.00,
        "Minute Maid: Fruit Punch": 2.00,
        "Fanta": 2.00,
        "Coffee": 3.00,
        "Iced Coffee": 3.50,
        "Dr. Pepper": 2.00,
        "Water": 1.00,
        "Salt Water": 1.50,
        "Chocolate Milkshake" : 7.50,
        "Vanilla Milkshake" : 7.45
    },
    "Main Course": {
        "Burger" : 15.00,
        "50 pounds of Sardines" : 10.00,
        "Cheese Burger": 15.10,
        "Pizza": 20.00,
        "Pasta" : 17.50,
        "Chicken Tenders" : 15.00,
        "Chicken Alfredo" : 18.00,
        "Chum": 0.50,
        "BLT Sandwich": 13.50,
        "BL Sandwich": 10.00,
        "B Sandwich": 7.50,
        "Roadhouse Burger": 17.50,
        "The Impossible Burger": 25.00,
        "The DOUBLE Impossible Burger": 30.00,
        "Route 77 Burger": 20.00,
        "Philly Cheese Steak" :20.00,
        "Ribs": 55.00,
        "Angus Beef Steak, with a Sardine" : 65.00,
        "Angus Beef Steak, without a Sardine" : 64.50
    },
    "Side Course" : {
        "Salad": 7.50,
        "Bacon": 5.00,
        "An Egg": 4.50,
        "Eggs" : 6.00,
        "Fries": 5.00,
        "Truffle Fries":10.00,
        "Mac & Cheese": 7.50,
        "2 Pounds of sardines": 3.00,
        "Sludge" : 3.00,
        "Brocoli and other vegitables": 6.50,
        "Bread": 3.50,
        "Calamari": 5.00
    },
    "Dessert" : {
        "Lava Cake": 16.75,
        "Water Cake": 15.75,
        "Sardine Cake": 10.00,
        "Pizookie": 15.00,
        "Banana Split": 15.00
    }
}
drinks = list(menu["Drinks"].keys())
main_items = list(menu["Main Course"].keys())
side_items = list(menu["Side Course"].keys())
desserts = list(menu["Dessert"].keys())
price_drinks = list(menu["Drinks"].values())
price_main = list(menu["Main Course"].values())
price_side = list(menu["Side Course"].values())
price_dessert = list(menu["Dessert"].values())

def waiter(number_choice):
    global waiter_name
    global waiter_personality
    if number_choice == 1:
        waiter_name = "Antonia"
        waiter_personality = "Brash"
        return waiter_name, waiter_personality
    elif number_choice == 2:
        waiter_name = "Nero"
        waiter_personality = "Calm"
        return waiter_name, waiter_personality
    elif number_choice == 3:
        waiter_name = "Icarus"
        waiter_personality = "Tsundere"
        return waiter_name, waiter_personality
    
def showMenu(name,personality):
    if name == "Antonia" and personality == "Brash":
        print('"Well bro, I should probably show you the menu! You came here to eat right? How lucky... I wish I could eat right now, but I already used all my food breaks for the day and the cook will propably kill me if I ask for another burger. Anyways here you go!" She says as she hands you the menu and waits paitently for you to order.')
        time.sleep(5)
        print("You read off the items in the menu.")
        print("You read the drink section... Then the Main Course section... Then the Side Course section... and lastly the desserts...")
        print("-" * 60)
        for i in range(0, len(drinks)):
            print(f"item name: {drinks[i]}. item price: {price_drinks[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(main_items)):
            print(f"item name: {main_items[i]}. Item price: {price_main[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(side_items)):
            print(f"item name: {side_items[i]}. Item price: {price_side[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(desserts)):
            print(f"Item name: {desserts[i]}.  Item price: {price_dessert[i]}")
            time.sleep(0.25)
    elif name == "Nero" and personality == "Calm":
        print('"Well anyways you came here to eat so I won\'t take up much of your time. Just order quick, Don\'t waste my time alright..." She rubs her forehead as she hands you the menu, you swear you could see steam come up from her head.')
        time.sleep(5)
        print("You read off the items in the menu.")
        print("You read the drink section... Then the Main Course section... Then the Side Course section... and lastly the desserts...")
        print("-" * 60)
        for i in range(0, len(drinks)):
            print(f"item name: {drinks[i]}. item price: {price_drinks[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(main_items)):
            print(f"item name: {main_items[i]}. Item price: {price_main[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(side_items)):
            print(f"item name: {side_items[i]}. Item price: {price_side[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(desserts)):
            print(f"Item name: {desserts[i]}.  Item price: {price_dessert[i]}")
            time.sleep(0.25)
    elif name == "Icarus" and personality== "Tsundere":
        print('"Here\'s the menu. It\'s sad that I have to be a waiter in a resturant considering the wealth my family holds, and to be placed in the same resturant as my rival Antonia... Just order already!!!!" He yells at you slightly before handing the menu to you, as his foot taps impatiently on the ground as you read it off.')
        time.sleep(5)
        print("You read off the items in the menu.")
        print("You read the drink section... Then the Main Course section... Then the Side Course section... and lastly the desserts...")
        print("-" * 60)
        for i in range(0, len(drinks)):
            print(f"item name: {drinks[i]}. item price: {price_drinks[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(main_items)):
            print(f"item name: {main_items[i]}. Item price: {price_main[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(side_items)):
            print(f"item name: {side_items[i]}. Item price: {price_side[i]}")
            time.sleep(0.25)
        print("-" * 60)
        for i in range(0,len(desserts)):
            print(f"Item name: {desserts[i]}.  Item price: {price_dessert[i]}")
            time.sleep(0.25)
        print("-" * 60)
   

def getOrder():
    global drink
    global main
    global side_one
    global side_two
    global dessert
    print("You think over what you want to get for some time... Everything sounds and looks good, besides the sardine items but who cares about those.")
    while True:
        try:
            drink = str(input("What will you get for you drink: "))
            if drink not in menu["Drinks"].keys():
                print("You don't think that's in the drink list.. maybe something else?")
                continue
        except ValueError:
            print("You consider changing your option...")
        else:
            break
    while True:
        try: 
            main = str(input("What will you get for your main course: "))
            if main not in menu["Main Course"].keys():
                print("You don't think that's in the main course list... maybe something else?")
                continue
        except ValueError:
            print("You consider changing your option...")
        else:
            break
    while True:
        try:
            side_one = str(input("What will you get for your first side: "))
            if side_one not in menu["Side Course"].keys():
                print("You don't think that's in the side course list... maybe something else?")
                continue
        except ValueError:
            print("You consider changing your option...")
        else:
            break
    while True:
        try:
            side_two = str(input("What will you get for your second side: "))
            if side_two not in menu["Side Course"].keys():
                print("You don't think that's in the side course list... maybe something else?")
                continue
        except ValueError:
            print("You consider changing your option...")
        else:
            break
    print("You consider getting dessert, before realizing that you'd love to get it!!!!")
    while True:
        try: 
            dessert = str(input("What will you get for your dessert: "))
            if dessert not in menu["Dessert"].keys():
                print("You don't think that's in the dessert list... maybe something else?")
                continue
        except ValueError:
            print("You consider changing your option...")
        else:
            break
    return drink, main, side_one, side_two, dessert
    


print("You enter a newly opened fancy resturant! Or what looks to be a fancy resturant... Anyways you sit down and wait to be greeted by a waiter.")
time.sleep(random.randint(1,10))
waiter_pick = random.randint(1,3)
waiter_name, waiter_personality = waiter(waiter_pick)
if waiter_name == "Antonia":
    print('"Hey bro!" You look up to see a somewhat chubby woman, who also looks pretty strong, who wears a suit like the rest of the staff here. "Hey, you gonna keep staring at me or what? Welp I\'m gonna be your waiter today. So just follow me! ')
    print("As you follow her to your table you look around the resturant, as you see a lot of people eat sardines... While Antonia yaps about the history of this resturant and how it used to be a sardine store. You notice Antonia has small red horns on her head, huh. While such things should be stranger, you just accept it.")
    time.sleep(random.randint(1,10))
    showMenu(waiter_name, waiter_personality)
    drink, main, side_one, side_two, dessert = getOrder()
    target_items = [drink, main, side_one, side_two, dessert]
    total = 0
    for item in target_items:
        if item in menu["Drinks"]:
            total += menu["Drinks"][item]
        elif item in menu["Main Course"]:
            total += menu["Main Course"][item]
        elif item in menu["Side Course"]:
            total += menu["Side Course"][item]
        elif item in menu["Dessert"]:
            total+= menu["Dessert"][item]
    total = round(total,2)
    print('"Well bro i\'ll get that for you! Just wait right here!" Antonia yells as she waves bye to you and goes off.')
    time.sleep(5)
    print("You see Antonia bug another waiter, with white hair and golden highlights in his hair. She puts her arm around him, only to get pushed off by the man who's now blushing heavily... you think to yourself:\"Just get me my food already bro\" ")
    time.sleep(random.randint(4,7))
    print("You finally see Antonia come with your food. The food looks like it may have been slightly eaten but who cares. And once you finally eat it, you're filled with pure happiness.")
    time.sleep(random.randint(4,7))
    print(f'"Welp you seem finished with your food!" You see Antonia now holding the check. "Well bro, your bill is {total}!')
elif waiter_name == "Nero":
    print('"Are you finished staring off into the distance?" You see a woman with a thin build, but looks fairly strong, and wears a suit like the rest of the staff here. "Well, I shall take you to your table. I am Nero, your waiter for today." ')
    print("As you follow her to your table you look around the resturant, as you see someone who's collapsed on a bucket of sardines on the table... While a child runs around... is this really a five star resturant? You see Nero hold out her leg, as the kid trips on it. You notice Nero has medium length blue horns on her head, and she's wearing a cast on her right arm. huh. You just accept it and hope the food is good.")
    time.sleep(random.randint(1,10))
    showMenu(waiter_name, waiter_personality)
    drink, main, side_one, side_two, dessert = getOrder()
    target_items = [drink, main, side_one, side_two, dessert]
    total = 0
    for item in target_items:
        if item in menu["Drinks"]:
            total += menu["Drinks"][item]
        elif item in menu["Main Course"]:
            total += menu["Main Course"][item]
        elif item in menu["Side Course"]:
            total += menu["Side Course"][item]
        elif item in menu["Dessert"]:
            total+= menu["Dessert"][item]
    total = round(total,2)
    print('"Well I shall get that for you. It won\'t take long I promise you." Nero nods at you as she goes off.')    
    time.sleep(5)
    print("You see Nero arm wrestle with another waiter with red horns. Looks like they are in a stalemate... You wonder to yourself how long it will take for your food to come in.")
    time.sleep(random.randint(5,7))
    print("Nero seems to head butt the waiter. This causes Nero to get kicked by the waiter, and Nero decides to finally get your food. Your food is slightly cold, but at least it still tastes amazing")
    time.sleep(random.randint(4,7))
    print(f'"Well it seems you have finished your meal." You see Nero holding the check. "Well your total bill is {total}.')
elif waiter_name == "Icarus":
    print('"Hey, you there? Well anyways I\'m Icarus Archer and your waiter for today..." He seems annoyed at your prescence, and grumbles the fact that he has to be a waiter. ')
    print("As you go to your table, Icarus talks to you about how honorable his family is and how they own this resurant and that he shouldn't work for them as just a simple waiter... You zone out most of what he says honesly. He talks about how much he dislikes one waiter here named Antonia... you really don't care. At least his hair looks nice with, with it being white and having golden highlights.")
    time.sleep(random.randint(1,10))
    showMenu(waiter_name, waiter_personality)
    drink, main, side_one, side_two, dessert = getOrder()
    target_items = [drink, main, side_one, side_two, dessert]
    total = 0
    for item in target_items:
        if item in menu["Drinks"]:
            total += menu["Drinks"][item]
        elif item in menu["Main Course"]:
            total += menu["Main Course"][item]
        elif item in menu["Side Course"]:
            total += menu["Side Course"][item]
        elif item in menu["Dessert"]:
            total+= menu["Dessert"][item]
    total = round(total,2)
    print('"Well whatever, I\'ll get it for you, ugh." Icarus stomps off, as he goes away.')
    time.sleep(5)
    print("You notice Icarus waiting at the kitchen, while a girl with red horns teases him. He's trying his best to ignore her, and failing at it. You wonder how long it will take you for your food to get here.")
    time.sleep(random.randint(4,7))
    print("Icarus finally arrives with your food. You eat the food with delight and bliss.")
    time.sleep(random.randint(4,7))
    print(f'"Are you finished yet?" You see Icarus holding the check. "Well anyways, your total bill is {total}.')
