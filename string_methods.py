# Santiago Pineda, String Methods

sentence = "The quick brown fox jumps over the lazy dog"


word = input("What word do you want?: " ).strip().lower()
new_word = input("What word should be in the sentence: ").strip().lowe()

location = sentence.find(word)
new_sentence = sentence.replace(word,new_word)

print(sentence.find("over"))

print(sentence.split('the'))

first_name = input("What is your first name: ").strip().title()
last_name = input("What is your last name: ").strip().title()
first_seperated_name = first_name.split()
first_fixed = "".join(first_seperated_name)
last_seperated = last_name.split()
last_fixed = "".join(last_seperated)
full_name = first_fixed.title() + " " + last_fixed.title()
print("Hello " +full_name.title())

print(full_name.isalpha) #Has to be all letters(no spaces too)
print(full_name.isnumeric) #Has to be all numbers
print(full_name.isupper) #has to be all uppercase


print(sentence.lower()) #all worda are in lower case
print(sentence.upper()) #all words are in upper case
print(sentence.capitalize()) #first word is capitalized
print(sentence.title()) #All first letters are capitalized
print(new_sentence)