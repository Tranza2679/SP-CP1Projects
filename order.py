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
    elif number_choice == 4:
        waiter_name = "Franco"


print("You enter a newly opened fancy resturant! Or what looks to be a fancy resturant... Anyways you sit down and wait to be greeted by a waiter.")
time.sleep(random.randint(1,10))
waiter_pick = random.randint(1,4)


#include random personalities for the waiters based on ocs:)))