# Santiago Pineda, Character Intro Assignment

character_name = input("Give me a character's name: ").strip().title()
character_age = input("Give me a character's age: ")
character_job = input("Give my character a job: ").strip().title()
character_location = input("Where is my character from: ").strip().title()
print("Hi my name is", character_name, "I am", character_age, "years old, I work as a",character_job + ", and I am from", character_location + ".")
