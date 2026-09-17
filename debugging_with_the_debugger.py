# Santiago Pineda, Debug with the Debugger
# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) #Runtime error: Quantity wasn't declared as an integer so it would give an incorrect result when we multipled.

total = price * quantity

discounted_total = total - (total * 0.10) #Logic error: the 10% discount wouldn't be properly applied.

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #Runtime Error: snack name should be snack_name and not snackName
print("Price per snack: " + str(price) + " credits")
print("Total before tax: "+ str(total)) #Logic Error: Instead of the total before the tax being written, it was the price which caused the wrong time to print out
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") #Syntax error: unclosed parenthesis caused the program to crash as a result.