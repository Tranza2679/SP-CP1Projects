# Santiago Pineda, for loop notes
import time #time is a library

# Iteration
siblings =  ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]
for sibling in siblings:
    print(f"Good Morning {sibling}")

grades = [100, 87, 53, 45, 78, 88, 3, 94]
average = 0

for grade in grades:
    average += grade 
    print(f"{grade} was added.")

average = average / len(grades)
print(f"Your average grade is {average:.2f}")

for i in range(1, 21): #Range builds a list for YOU, 
    print(i)
    time.sleep(.5) #Pauses your program for the number of seconds is put here, makes stuff slower ig

for i in range(20, 0, -1):
    print(i)
    time.sleep(.5)
    if i == 12:
        print("Wait it is lunch time")
        break