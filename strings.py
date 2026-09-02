# Santiago Pineda, String Notes

#Strings are a collection of characters held together by quotation marks

name = "Ms LaRose" #A string

age = "15" #ALSO a string

print(age + "2")

print(name + " " + age)

first_name = 'Vienna'
last_name = 'LaRose'
full_name = first_name + ' ' + last_name
print(full_name)
# Escape char (Tells the computer to ignore the next character)
sentence = 'Then he said "That isn\'t fair'
print(sentence)

sentence_two = '\t then he said \n "that isn\'t fair"'
print(sentence_two)
print("*" * 30)

sentence_three = "The quick brown fox jumps over the lazy dog"
print(sentence_three)
print(sentence_three.find("w"))
print(sentence_three[10:15]) # it's not 14 because doing this does NOT include the end point
word = input("what word do you want? ")
start = sentence_three.find(word)
length = len(word)
print(sentence_three[start:start + length])