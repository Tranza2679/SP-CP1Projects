# Santiago Pineda, Lists Tuples and Sets
#Lists
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"] #Every item has to be in brackets and seperated by commas. Every item MUST be a proper data type. This a complex data type as it holds multiple values and pieces of information at ONCE!!!
# lists have index numbers, for example Alex is at 0.
print(*siblings) # The * is the unpacking operator, it unpacks lists yo
print(f"My older sister is {siblings[1]}")
print(f"The youngest is {siblings[-1]}") # a - makes it go backwords

length = len(siblings)
siblings.append("Jayshree") #Append adds stuff to a list at the end
siblings.insert(3, "Vienna") #Insert adds it at a specific index number that you choose 
siblings.extend(["Joe", "Israel", "Zee"]) #Extend adds a list to a list
siblings.remove("Vienna")  #Removes based on item name
siblings.pop(0) #Removes based on index number, or the last one added
print(*siblings)

#Tuples
subjects = ("CP1", "CP2", "Advanced CP", "CSP", "Utah Studies", "US 1", "US 2", "World Civ", "World Geography", "CCA Business") #tuples used Parethesis
print(subjects[0])
print(*subjects)
subjects.append("Pyschology") #Tuples are immutiable, aka they really can't change!!!! Lists can obviously change. Lists are ordered and mutable(Changable) and Tuples are ordered. Lists and tuples can HAVE duplicates 

#SYMBOLS for lists are [], tuples uses () and sets used {}. Sets are unordered and mutable but does not ALLOW duplicates(Prevents us from having multiple of the same thing)

#SETS
visited = {"Texas", "Ohio", "Minnisoda", "Virginia", "D.C.", "Utah", "California", "Nevada"}
print(*visited) #IT prints in a different order EVERY single time
print(len(visited)) #You can find the lenght of it but can't use a exact location
visited.add("Idaho") #It just adds it wherever
visited.update({"Montana", "Arizona", "Oklahoma", "New Mexico"})
print(*visited)
visited.remove("Arizona")
print(*visited)

#These are collections. and you CAN convert them by using something like Set(variable name)