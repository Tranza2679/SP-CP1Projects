#Santiago Pineda, Unit 1 Final Project: Interactive Introduction Program Code
name = input("What is your name: ").strip().title()
location = input("What is your location: ").strip().title()
fav_hobby = input("What is your favorite hobby: ").strip().lower()
fav_food = input("What is your favorite food: ").strip().lower()
fav_media = input("What is your favorite piece of media: ").strip().title()
personality = input("How would you describe yourself in one word: ").strip().lower()

print("Hello! My name is " + name + ", and I live in " + location + ". My favorite hobby is " + fav_hobby + ". My favorite food to eat is " + fav_food + ". I like " + fav_media + ". I would personally say that I am " + personality + ". That is all about me!")