#Santiago Pineda, fix the game
import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        while True:
            try:
                guess = int(input("Guess a number between 1 and 20: "))
            except:
                print("You can't guess that!")
            else:
                guesses = guesses + 1
                break

        if guess == secret_number: #Syntax error, was missing a : which caused the code to break due to how you always need a : after an if.
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print("Your guesses per round: " + str(scores)) #Syntax error, you can't add a list to a string without changing it to a string.

total = 0
for score in scores:
    #Logic error, Due to total = 0 being placed here the total kept resetting so it would always end up as the last score and mess up the average
    total = total + score

average = round(total / rounds, 3)
print("Your average guesses per round was " + str(average))

best_round = scores[0]
for i in range(1, rounds ): #Logic error, the for loop never considered the last round so if the last round was the lowest then it would not be considered
    if scores[i] <= best_round: 
        best_round = scores[i] 

print(f"Your best round took only {best_round} guesses!")