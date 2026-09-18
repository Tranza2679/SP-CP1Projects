#Santiago Pineda, Crew Share
import random
num_of_pirates = 0
while True:
    try:
        num_of_pirates = int(input("How many pirates are on the crew, not including Yandu and Peter?"))
    except:
        print("Please write how many pirates there are properly")
    else:
        break

share = random.randint(500, 500)
first_cut = share - (num_of_pirates * 3)







































