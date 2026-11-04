#Santiago Pineda, Caesar cipher assignment 
def encoder(word):
    return word
    

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
    encoder(word_to_encode)
    print(word_to_encode)

    

elif choice == 2:
    pass