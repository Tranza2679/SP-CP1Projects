# Santiago Pineda, Debug with the Debugger
# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = input("How many would you like? ")

total = price * quantity

discounted_total = total - 2 * 0.10

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #Syntax error: Snake name should be snack_name and not snackName
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(price))
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") #Syntax error: The parenthesis weren't closed