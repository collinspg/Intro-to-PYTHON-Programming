word = "commitment"
print()
#favourite_letter = "m"
#print()
#for letter in word:
    #if letter == favourite_letter:
       # print(f"{letter.upper()}")
   # else:
       # print(f"{letter.lower()}")

#favourite_letter = input("Whats is your favourite letter?: ")
#print()
#for letter in word:
    #if letter.lower() == favourite_letter.lower():
        #print(letter.upper(), end="")
    #else:
        #print(letter.lower(), end="")
favourite_letter = input("Whats is your favourite letter?: ") 
print()
for letter in word:
    if letter.lower() == favourite_letter.lower():
        print("_",end="")
    else:
        print(letter.lower(), end="")
    