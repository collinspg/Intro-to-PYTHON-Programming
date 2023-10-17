secret = "python"
hint = "_" * len(secret)
guess_count = 0

print(f"Welcome to the word guessing game!\n")
print("Your hint is:", hint)


while True:
    # Creativity: I allowed user input to run regardless the case(Upper or lower) that is used.
    guess = input("What is your guess? ").lower()
    guess_count += 1

    if len(guess) != len(secret):
        print("Sorry, the guess must have the same number of letters as the secret word")
        continue
    if guess == secret:
        break

    new_hint = ""
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            new_hint += guess[i].upper()
        elif guess[i] in secret:
            new_hint += guess[i].lower()
        else:
            new_hint += "_"
    
    if new_hint != hint:
        hint =  new_hint
        print("Your hint is:", hint)

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guess(es).")

#creativity: I'm allowin the user to enter if they liked the game or not.
while True:
    enjoy_game = input(f"\nDid you enjoy the game? (Yes/No): ")
    if enjoy_game.lower() == "yes":
        print("Thank you for playing")
        break
    elif enjoy_game.lower() == "no":
        print("Sorry for the time you spent.")
        break
    else:
        print("Invalid response, please enter a 'Yes' or a 'No' ")
        continue

