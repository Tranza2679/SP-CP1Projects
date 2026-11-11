#Santiago Pineda, nesting notes

win = True
text = False
names = ["santi", "Antonia", "Icarus", "Nero", "Franco"]
favorite_foods = ["Pancakes", "Cake", "Steak"]

if win:
    if text:
        print("hallalujah")
    else:
        print("try again")
else:
    print("You failed")

for name in names:
    print(f"{name} is pretty cool")
    for food in favorite_foods:
        print(f"They love {food} with all their heart")

while True:
    for name in names:
        print(f"Helloa {name}!")
    again = input("Do you need to see them again: ")
    if again.lower() == "yes":
        pass
    else:
        break