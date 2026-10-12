# Santiago Pineda, Escape Room
locations = ["file cabinet" , "exit door", "hallway", "broken containment block", "morbid art piece"]
turn_count = 0
live = False
print("You are a researcher from Limbus Company. The day was supposed to go normally... just another day of researching abnormalities that the bus team had contained. Yet, everything that could have possibly went wrong infact did. Why did all of this happen? Well somehow some people were able to break in... why were they here? Well from what little you heard from the people that broke in, you remember hearing some beast of a man yelling \"Buddy!\" and some weird robot artist trying to make art out of some of the researchers... Welp, unluckily for you, you just so happened to have some spiral weapon attached into you with a 6 digit combination. Everytime you try to move, the spiral digs deeper into you, so you have to try to solve it soon or die trying...") 
while turn_count < 10:
    while True:
        try:
            user_choice = int(input("Will you\n 1: look around. 2: try to solve the code. "))
            if user_choice > 2:
                print("Well that's not a basic option you have... Please write the number it has been assigned...")
                continue
        except:
            print("That's not something you can do...")
        else:
            break
    if user_choice == 1:
        print("You look around and see a file cabinet laying on the floor, a door with a blinking exit sign on it, a hallway, a broken containment block, and a morbid art piece.")
        while True:
                try:
                    location_decision = int(input("Will you\n 1: Go to the file cabinet. 2: go to the exit door. 3: Go to the hallway. 4: Go to the Broken containment block. 5: Inspect the morbid art piece"))
                    if user_choice > 5:
                        print("Well that's not a basic option you have... ")
                        continue
                except:
                    print("That's not something you can do... Please write the number it has been assigned...")
                else:
                    break
        if location_decision == 1:
            turn_count =+ 1 
            print("You feel the spiral drill deeper into you... BUT you're at the file cabinet on the floor. There you see an assortment of files, but they seem to be a bit... messed up and slashed. Whoever is attacking this place really wanted to cause some damage.")

        elif user_choice == 2: 
            print("You look at the spiral, as you grab onto it. It seems to take a 6 digit number combo")

if live == False:
    print("The Spiral has drilled deep enough inside you and you die a slow and painful death. Which in all honesty, not the worst death you could have had... but I digress of course. Maybe in the next life you got it?")
elif live == True:
    print("You solved the combination and feel the spiral no longer drill into you as you take it off. You're still bleeding out though, BUT you find convientily placed bandadges and are able to stop the bleeding partially. Hey, at the very least if you live after this you'll be able to hopefully get some paid time off, which you probably will considering that you just saw most of your coworkers die... But I digress of course. ")