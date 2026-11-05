#Santiago Pineda, Caesar cipher assignment 

def encoder(words, shift):
    global number
    global new_word
    for i in range(0, len(words)):
        for word in words: 
            number = ord(word)
            number += shift
            word = chr(number)
            new_word = words.replace(word, words)
    return words


print("Hello user! Welcome to Caesar Cipher! With this program you can encode or decode!")
while True:
    try: 
        choice = int(input("What will you do? 1: encode or 2: decode "))
        if choice > 2:
            print("You really can't do that...")
            continue
    except:
        print("You really can't do that....")
    else:
        break

if choice == 1:
    word_to_encode = str(input("What word will you use? ")).strip()
    while True:
        try:
            number_to_shift = int(input("What number will you shift by? "))
        except:
            print("You can't shift by that number:(")
        else:
            break
    encoded_word = encoder(word_to_encode, number_to_shift)
    print(encoded_word)

    

elif choice == 2:
    pass