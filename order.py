#Santiago Pineda, Order Up!
import random
import time
waiter_name = ""
waiter_personality = ""

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
dessert = list(menu["Dessert"].keys())
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
    elif number_choice == 4:
        waiter_name = "Franco"
        waiter_personality = "Orderly"
        return waiter_name, waiter_personality
    elif number_choice == 5:
        waiter_name = "Verbena"
        waiter_personality = "Like Jabber"
        return waiter_name, waiter_personality
    
def showMenu(name,personality):
    if name == "Antonia" and personality == "Brash":
        print('"Well bro, I should probably show you the menu! You came here to eat right? How lucky... I wish I could eat right now, but I already used all my food breaks for the day and the cook will propably kill me if I ask for another burger. Anyways here you go!" She says as she hands you the menu and waits paitently for you to order.')
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
        for i in range(0,len(dessert)):
            print(f"Item name: {dessert[i]}.  Item price: {price_dessert[i]}")
            time.sleep(0.25)
    elif name == "Nero" and personality == "Calm":
        print('"Well anyways you came here to eat so I won\'t take up much of your time. Just order quick, Don\'t waste my time alright..." She rubs her forehead as she hands you the menu, you swear you could see steam come up from her head.')
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
        for i in range(0,len(dessert)):
            print(f"Item name: {dessert[i]}.  Item price: {price_dessert[i]}")
            time.sleep(0.25)
    elif name == "Icarus" and waiter_personality == "Tsundere":
        print('"Here\'s the menu. It\'s sad that I have to be a waiter in a resturant considering the wealth my family holds, and to be placed in the same resturant as my rival Antonia... Just order already!!!!" He yells at you slightly before handing the menu to you, as his foot taps impatiently on the ground as you read it off.')
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
        for i in range(0,len(dessert)):
            print(f"Item name: {dessert[i]}.  Item price: {price_dessert[i]}")
            time.sleep(0.25)
        print("-" * 60)
    elif name == "Franco" and waiter_personality == "Orderly":
        print('"Well boss, you came here to eat. I will not recommend you anything, as I\'m supposed to tell you that everything here is equally delicous. So I hope that you are able to decide for yourself. I am also inclined to tell you that this place was built on a resturant that sold only sardines, so after the purchase of this resturant we still have an ample amount of sardines to use to our disposal..." He trails off at the end, but hands you the menu as he paitently awaits your order.')
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
        for i in range(0,len(dessert)):
            print(f"Item name: {dessert[i]}.  Item price: {price_dessert[i]}")
            time.sleep(0.25)
        print("-" * 60)
    elif name == "Verbena" and waiter_personality == "Like Jabber":
        print('"Well, probably should give ya the menu. I don\'t suggest anything here being honest but you do you dawg. Here ya go, have fun choosing what poison you want." She hands you the menu, as she eyes the plant on your table')

print("You enter a newly opened fancy resturant! Or what looks to be a fancy resturant... Anyways you sit down and wait to be greeted by a waiter.")
#time.sleep(random.randint(1,10))
waiter_pick = random.randint(1,5)
waiter_name, waiter_personality = waiter(waiter_pick)


    




