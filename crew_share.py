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

share = random.randint(500,5000)
yondu_cut = round((share - (num_of_pirates * 3))* 0.13, 2)
peter_cut = round((share - yondu_cut - (num_of_pirates * 3)) * 0.11, 2)
crew_share = round((share - (yondu_cut + peter_cut) - (num_of_pirates * 3))/(num_of_pirates + 2), 2)
yondu_final = round(yondu_cut + crew_share, 2)
peter_final = round(peter_cut + crew_share, 2)

print(f"The units found: {share}")
print(f"Yondu's share: {yondu_final}")
print(f"Peter's share: {peter_final}")
print(f"Crew's share: {crew_share}")







































