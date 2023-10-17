cart = []
item_names = []
prices = []

print(f"Welcome to shopping cart program")

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
        amount = float(input(f"What is the price of {item}? "))
        cart.append(item)
        item_names.append(item)
        prices.append(amount)
        print(f"'{item}' has been added to the cart")
      
    elif action == 2:
        print("The contents of the shopping list are:")
        for i,  materials in enumerate(cart):
            print(f"{i+1}. {materials} - ${prices[i]:.2f}")

        # Creativity and exceeding requirements
        # I'm printing the statement below if there are no items in the shopping list.
        if len(cart) == 0:
            print(f"There are no items in the shopping list.")
        # End of Creativity and exceeding requirements.   

    elif action == 3:
        index = int(input("Which item would you like to remove? ")) - 1
        if index >= 0 and index < len(cart):
            item =cart.pop(index)
            price = prices.pop(index)
            print(f"'{item}' has been removed\n")
    # creativity and exceeding requirements
    # I'm using an else statement to display an invalid index action provided by the user.
        else:
            print(f"Invalid, Please enter a valid index.\n") # end of creativity and exceeding requirement.

       
    elif action == 4:
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}") 

    elif action == 5:
        print("Thank You. Goodbye.")
        break
    else:
        print(f"Sorry that is not a valid action.\n")

    