#Creativity will be the title of the game, and an instruction.
print(f"AMNESIA PART 2")
print(f"This game will ask the user to pick one out of three choices. Any choice not provided \nin the list is not accepted. Have fun! ")

#scenerio 1
print(f"\nYou are not sure who you are or where you are. All you know is that you are in a comfortable bed in a room you guess you could call comfortable. What should you do?: 'GO BACK TO SLEEP', 'LOOK THROUGH THE WINDOW', or 'FOLD SHEET' ")
choice = input("Choice: ")
if choice.lower() == "go back to sleep":
    print(f"The bed is very comfortable, but you are not necessarily ready to go back to sleep \nas you are kind of wondering who and where you are remember? 'YES', 'NO', 'A LITTLE' ")

#scenerio 2/ nested if to continue story for choice 1
    choice_2 = input("Choice:")
    if choice_2.lower() == "yes":       
        print(f"You decided to find out who or where you are. You approached the door, you feel \nthis door would be very important to open. Opening this door \nwill probably propel this story this most. The door is a gateway \nfrom your current placement into a grand adventure. You observe your door is blocked by a large object. \nThis door to put it bluntly, is TOTES MCGOATS! What should you do? \n 'SLEEP', 'SCREAM', or 'BE FRUSTRATED' ") 
#scenerio 3 for choice 2         
        choice_3 = input("Choice: ") 
        if choice_3.lower() == "sleep":
            print(f"I will go back to sleep.")
        elif choice_3.lower() == "scream":
            print(f"I will scream.")
        elif choice_3.lower() == "be frustrated":
            print(f"I will be frustrated.")
        else:
            print(f"Error, Please enter a correct choice: 'SLEEP', 'SCREAM', or 'BE FRUSTRATED' ")
    elif choice_2.lower() == "no":
        print(f"This becomes hard for you, because you don't even know you have amnesia. I wonder \n if you would even know who a doctor is with your state. You heard a voice. \nWhat will you say? 'HELLO', 'STAY AWAY', or 'I DON'T KNOW'  ")
        choice_3i = input("Choice: ")
        if choice_3i.lower() == "hello":
            print(f"Hello! Who is there.")
        elif choice_3i.lower() == "stay away":
            print(f"Please stay away.")
        elif choice_3i.lower() == "i don't know":
            print(f"I don't know what to say.")
        else:
            print(f"Error, Please enter a correct choice: 'HELLO', 'STAY AWAY' or 'I DON't KNOW' ")
    elif choice_2.lower() ==  "a little":
        print(f"You even more confused because you have different shades of memory and the only word \nyou remember is 'LOVE', 'HATE', or 'FRIEND' ")       
        #nested if for more story
        choice_3ii = input("Choice: ")
        if choice_3ii.lower() == "love":
            print(f"I love myself.")
        elif choice_3ii.lower() == "hate":
            print(f"I hate myself.")
        elif choice_3ii.lower() == "friend":
            print(f"I have no friends.")
        else:
            print(f"Error, Please enter a correct choice: 'LOVE', 'HATE', or 'FRIEND'.")
    else:
        print(f"Error, Please enter a correct choice: 'YES', 'NO', or 'A LITTLE'  ")


#Else if statement for scenerio 1/nested else if to continue story
elif choice.lower() == 'look through the window':    
    print(f"You look out the window. it is bullet proof, which you may or may not know because \nof your amnesia. And even if you did understand bullet proof \nglass, would you recognize it? You are not sure, on account of your \namnesia. You decided to 'HIT', 'SHOOT', or 'BEND' ")
#scenerio 2/nested if to continue stroy for choice 1    
    choice_ii = input("Choice: ")
    if choice_ii.lower() == "hit":       
        print(f"You tried to hit the glass to be sure it is a bullet proof glass, but you soon \nbegan to cry because you thought that your whole world would be \nshattered if it were not a bullet proof glass and that the glass gets broken eventually. \nWhat will you do? 'STOP', CONTINUE', or 'DANCE' ")
#scenerio 3 for choice 2          
        choice_iii = input("Choice: ")
        if choice_iii.lower() == "stop":
            print(f"I will stop the game.")
        elif choice_iii.lower() == "continue":
            print(f"I will continue the game.")
        elif choice_iii.lower() == "dance":
            print(f"I will begin to dance.")    
        else:
            print(f"Error, Please enter a correct choice: 'STOP', 'CONTINUE' or 'DANCE' ")

    elif choice_ii.lower() == "shoot":
        print(f"You stood up, picked up the gun you had beneath the bed, you looked at the window \nagain, you wondered if the bullets were going to penetrate \n you took a shot and boom the bullet broke the glass.What will you do? \n 'JUMP','SIT', or 'LAUGH' ")
    #scenerio 3 for choice 2    
        choice_iv = input("Choice:")
        if choice_iv.lower() == "jump":
            print(f"I will jump out of the window.")
        elif choice_iv.lower() == "sit":
            print(f"I will sit")
        elif choice_iv.lower() == 'laugh':
            print(f"I will laugh the whole day")
        else:
            print(f"Error, Please enter a correct choice: 'JUMP', 'SIT', or 'LAUGH' ")
    
    elif choice_ii.lower() == 'bend':
        print(f"You bent down after considering a lot of factors and decided to 'DISCONTINUE', 'CONTINUE WITH FRIENDS', or 'START AFRESH' ")
        choice_v = input("Choice:")
        #nested if for more story
        if choice_v.lower() == "discontinue":
            print(f"You are tired of playing, you called you friends but none was \nwilling to play so you discontinued the game. ")
        elif choice_v.lower() == "continue with friends":
            print(f"The game interests you, you called unto your friends, and you all continued the game.")
        elif choice_v.lower() == 'start afresh':
            print(f"You don't like the particuar choice you picked so you started afresh.")
        else:
            print(f"Error, Please enter a correct choice: 'DISCONTINUE', 'CONTINUE WITH FRIENDS', or 'START AFRESH' ")
    else:
        print(f"Error, Please enter a correct choice: 'HIT','SHOOT', or 'BEND' ")

#Else if statement for scenerio 1/nested else if to continue story 
elif choice.lower() == "fold sheet":
    print(f"You proceeded in doing exercise, after that you ended up folding the bed sheet \nand  discovered that you are good at folding things. It may \nreally not probably help you in a job or occupation, but you may 'MAKE', 'TAKE' or 'EXAMINE' ")  
    #scenerio 3 for choice 2

    response = input("Choice: ")  
    if response.lower() == "make":
        print(f"but you may make a boring party trick. You are able to fold the sheet and \nsome pieces of paper small enough to fit into your pocket. \nYou have to eat sevaral truffles to make them fit, though, you were getting hungry anyway. \n you decided to 'EAT', 'SPIT' or 'SWALLOW' ")
        #nested if for more story
        response_1 = input("Choice: ")
        if response_1.lower() == "eat":
            print(f"I decided to eat good foods afterwards.")
        elif response_1.lower() == "spit":
            print(f"I decided to spit the papers I had eaten.")
        elif response_1.lower() == "swallow":
            print(f"I decided to swallow the papers that I had eaten.")
        else:
            print(f"Error, Please enter a correct choice: 'EAT', 'SPIT', or 'SWALLOW' ")


    elif response.lower() == 'take':
        print(f"but you may take too much time before you realise that you are folding the \nsheet in the wrong way. You decided to let go and you began walking away. \nWhen you looked back you saw a beautiful lady and you decided to 'TALK', 'IGNORE', or 'KISS'")  
        #nested if for more story.
        response_2 = input("Choice: ")  
        if response_2.lower() == "talk":
            print(f"You decided to talk to the lady, you talked for a long time and then you \nrealized that you had never been happy the whole time until you talked to her.")
        elif response_2.lower() == "ignore":
            print(f"You decided to ignore the lady because you were begining to remember that \nit was the amnesai that might have brought her to you. Yet you contemplated within you \nif it was a good idea to ignore her.")  
        elif response_2.lower() == "kiss":
            print(f"You decided to take a bold step to kiss her. The moment you felt her hands \nand tried to kiss her, she vanished from before you and you wondered \nwhere she had gone.")
        else:
            print(f"Error, please enter a correct choice: 'TALK', 'IGNORE', or 'KISS' ")


    elif response.lower() == 'examine':
        print(f"but you may loose focus, because you have examined that the room was full of \nwires. There is a computer resting on the desk. In the corner there is \na strong device, connected to a large eight foot tall oval frame.You thought of 'PLAYING', 'WATCHING', or 'READING' ")
        #nested if for more story
        response_3 = input("Choice: ")
        if response_3.lower() == "playing":
            print(f"You turned on the computer and decided to play video games on the computer.")
        elif response_3.lower() == "watching":
            print(f"You turned on the computer and decided to watch Hollywood movies on NetFlix.")
        elif response_3.lower() == "reading":
            print(f"You turned on the computer and decided to read about the political affairs  \nof Nigeria from the internet.")
        else:
            print(f"Error, Please enter a correct choice: 'PLAYING', 'WATCHING', or 'READING'")
    else:
        print(f"Error, Please enter a correct choice: 'MAKE', 'TAKE', or 'EXAMINE' ")
#Else statements for scenerio 1
else:
    print(f"Error, Please enter a correct choice:'GO BACK TO SLEEP', 'LOOK THROUGH THE WINDOW', or 'FOLD SHEET' ")