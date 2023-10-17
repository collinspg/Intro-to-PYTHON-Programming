cart = []

print("Welcome to shopping cart program")
while True:
    print(f"\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. quit")

    action = int(input("Please enter an action: "))

    if action == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to the cart")
      
    elif action == 2:
        print("The contents of the shopping list are:")
        for item in cart:
            print(item)
            
    elif action == 5:
        print("Thank You. Goodbye.")
        break

    else:
        print(f"Sorry that is not a valid action.\n")
    

