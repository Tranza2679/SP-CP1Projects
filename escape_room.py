# Santiago Pineda, Escape Room
import time

locations = ["file cabinet" , "exit door", "hallway", "morbid art piece"]
combination = 404957
live = False

def turnCountIncreasor(first_time):
    global full_count
    if first_time:
        full_count = 0
    else:
        full_count += 1
        print(f"You have done {full_count} actions out of 10.")
        return full_count



turnCountIncreasor(True)
print("You are a researcher from Limbus Company. The day was supposed to go normally... just another day of researching abnormalities that the bus team had contained. Yet, everything that could have possibly went wrong infact did. Why did all of this happen? Well somehow some people were able to break in... why were they here? Well from what little you heard from the people that broke in, you remember hearing some beast of a man yelling \"Buddy!\" and some weird robot artist trying to make art out of some of the researchers... Welp, unluckily for you, you just so happened to have some spiral weapon attached into you with a 6 digit combination. Everytime you try to move, the spiral digs deeper into you, so you have to try to solve it soon or die trying...") 
while full_count < 10:
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
        print("Note, if you have already visited a location then you cannot visit it again. Why? welp, it's impossibleeeeee...... ")
        while True:
                try:
                    location_decision = int(input("Will you\n 1: Go to the file cabinet. 2: go to the exit door. 3: Go to the hallway. 4: Inspect the morbid art piece. "))
                    if location_decision > 4:
                        print("Well that's not a basic option you have... ")
                        continue
                except:
                    print("That's not something you can do... Please write the number it has been assigned...")
                else:
                    break
        if location_decision == 1 and "file cabinet" in locations:
            turnCountIncreasor(False)
            print("You feel the spiral drill deeper into you... BUT you're at the file cabinet on the floor. There you see an assortment of files, but they seem to be a bit... messed up and slashed. Whoever is attacking this place really wanted to cause some damage.") 
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
                turnCountIncreasor(False)
            elif inspect_files == 2:
                print("You look around, and find a lot of employees that are unresponsive. You check the current time of a digital clock, seems it was on a timer that reached its end. The clock isn't necessarily ringing out loudly, but most of the numbers on it have been cut and only the second number is shown which is a 0.")
                locations.remove("file cabinet")
                turnCountIncreasor(False)

        elif location_decision == 2 and "exit door" in locations:
            print("You notice the exit door, though you wonder if you could actually run to it.")
            while True:
                try:
                    run_or_not= int(input("Will you really run to the door? \n 1: Yes. 2: Absolutely not"))
                    if run_or_not > 3:
                        print("Well that's not a basic option you have... Please write the number it has been assigned...")
                        continue
                except:
                    print("That's not something you can do... Please write the number it has been assigned...")
                else:
                    break
            if run_or_not == 1:
                print("You attempt running to the exit door. You do know you have something that hurts you if you move a lot currently on you, you know? It wasn't a necessarily bad idea, but not a good one. Just as you are about to open the door, you notice that the spiral had drilled deep inside you.")
                locations.remove("exit door")
                break
            elif run_or_not == 2:
                print("You realize that running with your current circumstances, would not end well. But while you look away you notice 5 people who attempted to run to the exit door. Maybe that's something to note.")
                locations.remove("exit door")
                turnCountIncreasor(False)
        elif location_decision == 3 and "hallway" in locations:
            print("You walk in the hallway. Or really just walking for a moment before looking around. You look around 3 different rooms. One has a beautiful hue of teal. One has what seems to be... electronic music playing? One has a good amount of people talking. ")
            while True:
                try:
                    where_to_go = int(input("Where will you go? \n 1: room with a beautiful hue of teal. 2: room with electronic music playing. 3: room with people talking."))
                    if where_to_go > 3:
                        print("Hey, you can't do that?")
                        continue
                except:
                    print("Well that's not a basic option you have... Please write the number it has been assigned...")
                else:
                    break
            if where_to_go == 1:
                print("You are allured by the beautiful hue of teal. You endlessely walk to it, forgetting all about the spiral. Eventually you do find what it was, as a small fairy touches your hand. However, you walked too much and wasted all of your actions")
                break
            elif where_to_go == 2:
                print("You enter that room. There you are met by a girl wearing a large white winter jacket, with chains on her arms that don't really seem to be affecting her. The music is coming from a small boombox on her hip. She notices you and for a moment is about to cut you with a sword before shrugging. \"Yo bro, you really ain't looking good no cap. Oh you got one of those spiral things, I would help you if I actually knew the code but lowkey I don't. But I remember hearing robo unc talk about how it was Yoshihide's birthday. You know who that is? she apparently took on some new name, Ryoshu or something, honestly pretty auraful. Am I right?\"")
                print("Well, after she continued yapping about how cool this Ryoshu is you were able to find a moment to sneak away. At least you know what the code is, technically. Maybe you might find more stuff if you go to the file cabinet if you haven't gone there already...")
                turnCountIncreasor(False)
            else:
                print("As you attempt to enter the room, the door closes. However, you can still hear the people talking. Seems they are also trying to remove the device as well, and got one part of the code being 4 and 9. They know that there are two 4s that have a number in between them.")
                turnCountIncreasor(False)
        elif location_decision == 4 and "morbid art piece" in locations:
            print("You go to the morbid art piece nearby. You feel an urge to throw up immediately, but you hold it in. You cover your eyes from the piece so you don't see it much.")
            while True:
                try:
                    inspect_art = int(input("What will you do? 1: Inspect the art piece for clues. 2: Leave and return"))
                    if inspect_art > 2:
                        print("Not an option you have... please pick something else.")
                        continue
                except:
                    print("Well that's not a basic option you have... Please write the number it has been assigned...")
                else: 
                    break
                turnCountIncreasor(False)
                if inspect_art == 1:
                    print("You inspect it more. You no longer feel the need to throw up, but you realize that the art piece... isn't good. All it could be described are pieces put together and ordered neatly, sure its art but it's just not interesting. Though you see some pieces of bones around that read, \"Dedicated to my dear Yoshihide. A gift to you for your birthday, April 4th.\"")
                    turnCountIncreasor(False)
                elif inspect_art == 2:
                    print("You leave the morbid art piece alone. Maybe it was for the better. Though you notice that there's 95 pieces of bones around it. A weird detail isn't it? ")
                    turnCountIncreasor(False)

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
            turnCountIncreasor(False)

    else:
        print("How did you possibly get here? Well if this somehow happened, then you deserve what happens next")
        break

    if full_count == 5:
        print("A man in a suit walks past you. You play dead out of fear for who this man is. He moves calmy, as an intercom rings out. The intercom rings out, with your boss saying \"All employees, reinforcements are coming in apporximately 957 seconds and the attack will be put to an end.\" The man looks at the intercom for a moment before slashing it with a weapon you could not see, he says something quietly about how ironic that number is")
    elif full_count == 8:
        print("You don't have much actions remaining. But the robot artist can be heard nearby... making some more artwork. He hums a tune, a nice one, but still eerie nonetheless. He says something about his daughter, being born on April, maybe thats 'important.'")



if live == False:
    print("The Spiral has drilled deep enough inside you where any other move would result in your death. You're forced to just lay on a wall, taking slow breaths to not cause it to go deeper. Maybe in the next life you got it? Who really knows.")
elif live == True:
    print("You solved the combination and feel the spiral no longer drill into you as you take it off. You're still bleeding out though, BUT you find convientily placed bandadges and are able to stop the bleeding partially. Hey, at the very least if you live after this you'll be able to hopefully get some paid time off, which you probably will considering that you just saw most of your coworkers die... But I digress of course. ")