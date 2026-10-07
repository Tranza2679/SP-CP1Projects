# Santiago Pineda, Mapping Notes
import math
def times(num):
    return num * 2

numbers = range(1,6)

multiply_numbers = map(times, numbers) #First part has to be a function and the second part has to be a function

print(*list(multiply_numbers))

new_numbers = []
for number in numbers:
    new_numbers.append(number*2)

print(*new_numbers)

siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

length = list(map(len, siblings))
print(length)

print(math.factorial(5))