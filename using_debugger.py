# Santiago Pineda, using the debugger

grades = [85, 90, 78, 92, 88]

total = 0
count = len(grades)
for grade in grades: 
    total = total + grade

average = total / count 

print(f"The average grade is {average}")

scores = [12, 45, 7, 68, 33, 90, 21]

running_total = 0
highest_score = 0

for score in scores:
    running_total += score
    if score > highest_score:
        highest_score = score

print(f"total: {running_total}")
print(f"Highest score: {highest_score}")