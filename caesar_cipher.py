#Santiago Pineda, Caesar cipher assignment 

def encoder(words, shift): #This function is meant to encode a letter by adding the shift number to its ord value
    global new_word
    global shifted_word
    global number
    new_word = []
    for word in words: #this loop checks every character in a given word
        number = ord("A") if word.isupper() else ord("a") #Makes it wrap around correctly as the asky values for a capital and lowercase letter is different
        shifted_word = chr((ord(word) - number + shift) % 26 + number) #This part is the encoded word and the wrap around with % 26 making it so it will wrap around the chracters in the alphabet
        new_word.append(shifted_word)
    return "".join(new_word) #Returns the final word correctly as a string rather than a list of seperate characters

def decoder(words,shift):
    new_word = []
    for word in words: 
            number = ord("A") if word.isupper() else ord("a") 
            shifted_word = chr((ord(word) - number - shift) % 26  + number) 
            new_word.append(shifted_word)
    return "".join(new_word)

while True:
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
        print(f"Your encoded word is: {encoded_word}" )

    elif choice == 2:
        word_to_decode = str(input("What word will you decode? ")).strip()
        while True:
            try:
                number_to_shift = int(input("What number will you shift by? "))
            except:
                print("You can't shift by that number:(")
            else:
                break
        decoded_word = decoder(word_to_decode,number_to_shift)
        print(f"Your decoded word is: {decoded_word}")
       
