# Integers and Float notes, Santiago Pineda

# integer - a whole number
num = 75 # <= Just write the number no extra syntax

# Float # <= a number with a decimal point 
pi = 3.1415 # <= Just write the number no extra syntax

# Arithmetic Operators ( + - * / ** // %) ** is for exponents, // is for integer division and % is modulo 
print( 4 +2 )
print(5//2) # <= Integer division (it only gives you the integer)
print(5/2) #<= will always output a float

# modulo = %
print( 5%2)
print(10%3)
print(15%5) # modulo gives the remainder of a division problem. Also known as mod and % is known as modulus 

print((2-1)*3+4%3)
# Order of Operations (P E MMD AS) 

# assignment operator = 
 
fav = float(input("What is your favorite number: "))

print(f"{float(fav)**2} is {fav} squared!")
print(round(pi,2))
print(int(pi)) 