# Santiago Pineda, Escape Room
import time

locations = ["file cabinet" , "exit door", "hallway", "broken containment block", "morbid art piece"]
turn_count = 0
combination = 404957
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
        print("Note, if you have already visited a location then you cannot visit it again. Why? Well, the Spiral would not like that, how would it know? A question for another day. Just don't attempt to visit a location again, or you will deviate from the path. ")
        while True:
                try:
                    location_decision = int(input("Will you\n 1: Go to the file cabinet. 2: go to the exit door. 3: Go to the hallway. 4: Go to the Broken containment block. 5: Inspect the morbid art piece"))
                    if location_decision > 5:
                        print("Well that's not a basic option you have... ")
                        continue
                except:
                    print("That's not something you can do... Please write the number it has been assigned...")
                else:
                    break
        if location_decision == 1 and "file cabinet" in locations:
            turn_count =+ 1 
            print("You feel the spiral drill deeper into you... BUT you're at the file cabinet on the floor. There you see an assortment of files, but they seem to be a bit... messed up and slashed. Whoever is attacking this place really wanted to cause some damage.") 
            print(f"You have done {turn_count} actions ")
            while True:
                try:
                    inspect_files = int(input("Will you\n 1: Inspect the files. 2: walk around some more"))
                    if inspect_files> 2:
                        print("Well that's not a basic option you have... Please write the number it has been assigned...")
                        continue
                except:
                    print("That's not something you can do... Please write the number it has been assigned...")
                else:
                    break
            if inspect_files == 1:
                print("You look through the files. All it seems to be are records of employees. You read quickly three files. One was a friend of yours, they got changed to another department of the company back 5 years ago. Another file is about an abnormality, though for some reason after reading the name of it you feel an urge to stop reading that file. You find a file of a employee from the Bus department, most of the information is slashed besides their name being \"Ryoshu\" and their birthday being on April, but the exact date is cut apart.")
                locations.remove("file cabinet")
                turn_count =+ (1 + turn_count)
                print(f"The spiral drills deeper in, you have done {turn_count} actions out of 10")
            elif inspect_files == 2:
                print("You look around, and find a lot of employees that are unresponsive. You check the current time of a digital clock, seems it was on a timer that reached its end. The clock isn't necessarily ringing out loudly, but most of the numbers on it have been cut and only the second number is shown which is a 0.")
                locations.remove("file cabinet")
                turn_count =+ (1 + turn_count)
                print(f"The spiral drills deeper in, you have done {turn_count} actions out of 10")
            
            elif location_decision == 2 and "exit door" in locations:
                print("Poop")

    elif user_choice == 2: 
        print("You look at the spiral, as you grab onto it. It seems to take a 6 digit number combo")
        while True:
            try:
                code_try = int(input("What will you attempt to put in? "))
                if code_try > 999999:
                    print("It only has six numbers you can put in it... How would you even put in more than that?????")
                    continue
            except:
                print("How could you possibly put that in? Maybe rethink some stuff....")
            else:
                break
        if code_try == combination:
            print("Hey, it seems that was the right code all along. Great job")
            live = True
            break
        else:
            print("Welp, you got the code wrong. A for effort though! Even if there is no A in effort.... But the spiral does drill deeper.")
            turn_count += 1
    else:
        print("How did you possibly get here? Well if this somehow happened, then you deserve what happens next")
        break
    if turn_count == 5:
        print("A man in a suit walks past you. You play dead out of fear for who this man is. He moves calmy, as an intercom rings out. The intercom rings out, with your boss saying \"All employees, reinforcements are coming in apporximately 957 seconds and the attack will be put to an end.\" You feel that ")

if live == False:
    print("The Spiral has drilled deep enough inside you where any other move would result in your death. You're forced to just lay on a wall, taking slow breaths to not cause it to go deeper. Maybe in the next life you got it? Who really knows.")
elif live == True:
    print("You solved the combination and feel the spiral no longer drill into you as you take it off. You're still bleeding out though, BUT you find convientily placed bandadges and are able to stop the bleeding partially. Hey, at the very least if you live after this you'll be able to hopefully get some paid time off, which you probably will considering that you just saw most of your coworkers die... But I digress of course. ")