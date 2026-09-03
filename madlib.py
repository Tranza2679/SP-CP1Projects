# Santiago Pineda, Madlib 
print("Hello! welcome to my madlib!")
animal = input("Give me the name of any animal: ").strip().lower()
verb = input("Give me a verb that ends in ing ").strip().lower()
second_animal = input("Give me the name of another animal(could be the same as the last): ")
adjective = input("Give me an adjective to describe the animal you wrote in the last question: ").strip().lower()
second_verb = input("Give me a verb: ").strip().lower()
location = input("Give me a location: ").strip().title()
activity = input("Give me an activity: ").strip().lower()
objects = input("Give me an object: ").strip().lower()

sentence = "Suddenly one day, " + animal + " had found themselves " + verb + " all by their lonesome.\nYet to their surprise they had found a friend who was a " + second_animal + ", they were quite wholesome.\nThe "  + animal + "'s buddy had a " + adjective + " idea, one that only it could make.\nThe " + second_animal + " had decided that the both of them would try " + second_verb +" at " + location + ", they hoped their plan would not be a mistake.\nAs they walked to " + location + ", they had both decided they would also try to partake in " + activity +".\nHowever, once they had arrived they met an angry mob of protesters who were advocating for banning all instances of " + activity + " being done at " + location + ", so the angry mob had thrown " + objects + " at both of the friends." 
print(sentence)