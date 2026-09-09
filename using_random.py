import random
#randint lets you get a random integer, but needs two pieces of info aka the lowest number possible and highest number possible. Randit is a function we get from import random, and it takes 2 arguments and returns the value that ducks becomes
ducks = random.randint(1,10)

print(f"There are {ducks} ducks!")

pens = random.randrange(2,10,2) #Randrange needs a start(first argument), end(second arguments, its not included here) , stop point is not included) and the step number aka what it is counting it by(last arguments)
print(f"I have {pens} pens.")

boring_pens = random.randrange(1,15,3) 
print(f"I have {boring_pens} boring pens")

percent = random.random() #DOES NOT TAKE ANY ARGUMENTS!!!!!!!!!!!!!!!!!!!!!!!!!! random is our function, and it gives a random decimal between 0 AND 1. Gives a float. 

print(f"You have a {percent:.2} grade") #FLoats don't register the 0, so while there are 3 values here it thinks there are only 2. 