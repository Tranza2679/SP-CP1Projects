# Santiago Pineda, While Loops
#A while loop will continue running until a condition is met

import random
import time

goose = random.randint(1,20)
duck = 1 #Start Point

while goose > duck: #End Point
    print("Duck....")
    time.sleep(0.1)
    duck += 1 #Incrimentor, used to change the iterator or what is the current iretation of the loop. 
    if duck == 15:
        print("Game Over")
        break
else: #Else will only happen if the loop ends naturally and not by anything such as a break
    print("Goose!")


count = 1

while count >= -30:
    print(count)
    time.sleep(.1)
    count -= 1

number = random.randint(1,101)

while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 0 or guess > 100:
                print("You should read the intructions!")
                continue #Restarts the loop, starts the next iteration
            break
        except:
            print("That isn't a number")
    if guess == number:
        print("You got the number correct, you win!")
        break
    elif guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("I don't")