print("You are not sure who you are or where you are. All you know is that you are in a comfortable bed in a room you guess you could call comfortable. What should you do?: 'GO BACK TO SLEEP' or 'LOOK THROGH THE WINDOW' ")
choice = input("Choice: ")
if choice.lower() == "go back to sleep":
    print(f"The bed is very comfortable, but you are not necessarily ready to go back to sleep \nas you are kind of wondering who and where you are remember?  ")
elif choice.lower() == 'look through the window':    
    print(f"You look out the window. it is bullet proof, which you may or may not know because \nof your amnesia. And even if you did understand bullet proof \nglass, would you recognize it? You are not sure, on account of your \namnesia.")
else:
    print(f"Error, Please enter a correct choice:'GO BACK TO BED' or 'LOOK THROUGH THE WINDOW'")