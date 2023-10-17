print(f"Welcome to the word guessing game!\n")
secret = "python"
guess = ""
guess_count = 0
while guess != secret:
    guess = input("What is your guess? ")
    guess_count += 1
    if guess == secret:
        print(f"Congratulations! You guessed it!")
    else:
        print(f"Your guess was not correct.")
print(f"It took you {guess_count} guesses.")