# Method 1
# This Function displays a message in its regular texts

def display_regular(message):
    print(message)

# This Function displays a message in Uppercase texts
def display_uppercase(message):
    upper_case_message = message.upper()
    print(upper_case_message)

# This Function displays a message in Lowercase texts
def display_lowercase(message):
    lower_case_message = message.lower()
    print(lower_case_message)

# Allows users to enter a message and continue to run program if the user wants to enter another message until they quit
#prints all results and adding the messages to their contexts.
while True:
    user_message = input("Enter a message (or 'exit' to quit): ")

    if user_message.lower() == "exit":
        break

    display_regular(user_message)
    display_uppercase(user_message)
    display_lowercase(user_message)




#Method 2
# This Function displays a message in its regular texts
# def display_regular(message):
#      print(message)

# This Function displays a message in Uppercase texts
# def display_uppercase(message):
#      print(message.upper())

# This Function displays a message in Lowercase texts
# def display_lowercase(message):
#      print(message.lower())
     
    

# Allows users to enter a message and continue to run program if the user wants to enter another message until they quit
#prints all results and adding the messages to their contexts.
# while True:
#     user_message = input("Enter a message (or 'exit' to quit): ")

#     if user_message.lower() == "exit":
#         break

#     display_regular(user_message)
#     display_uppercase(user_message)
#     display_lowercase(user_message)