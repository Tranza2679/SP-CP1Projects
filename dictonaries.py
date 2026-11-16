#Santiago Pineda, dictonaries notes

#Collection of key and value pairs 

car = {
    "make": "Jeep",
    "model":"Wrangler",
    "color": "Silver", 
    "year": 2023
}

keys = list(car.keys()) #Gets you all the keys
values = list(car.values()) #Gets you all the values
print(*car)
print(car["make"]) # This is how we get individual items! Woah!
print(list(car.keys())) #Gives us the list of all the keys 
for key in keys:
    print(f"{key} is {car[key]}")

print(values)
print(len(car)) #Tells you how much values there is for the keys...

if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"

keys = list(car.keys())
for key in keys:
    print(f"{key} is {car[key]}")

avatar = {
    "Water": {
        "Katara" : "Water bender",
        "Sokka" : "Leader", 
    },
    "Earth": {
        "Toph" : "Earth bender. The GOAT!"
    },
    "Air": {
        "Aang": "Air bender, the Avatar"
    },
    "Fire": {
        "Zuko": "Fire bender, future fire lord",
        "Iroh": "The actual GOAT. Fire bender, Dragon of the west",
        "Azula": "Fire lord for 1 hour. Amazing fire bender"
    }
}

print(avatar["Fire"]["Iroh"])
print(avatar.get("Earth").get("Toph"))