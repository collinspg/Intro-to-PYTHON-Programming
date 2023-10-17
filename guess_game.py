import random
play_again = "yes"

#stretch challenge
while play_again.lower() == "yes":
    magic_number = random.randint(1, 100)
    guess_number = 0
    guess_count = 0
#core_requirement
    while guess_number != magic_number:
        guess_number = int(input("What is your guess? "))
        guess_count = guess_count + 1
        if guess_number == magic_number:
            print("You guessed it!")
        elif guess_number > magic_number:
            print("Guess Lower")
        else:
            print("Guess Higher")
    print(f"It took you {guess_count} guesses")
    play_again = input("Would you like to play again (Yes/No)? ")

print("Thank You for playing. Goodbye")

