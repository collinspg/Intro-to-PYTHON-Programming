print("Please enter the items of the shopping list (type: quit to finish): ")
shopping_list = []
items = ""

while items != "quit":
    items = input("Items: ")

    if items != "quit":
        shopping_list.append(items)

print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

index = int(input("Which item would you like to change?: "))
new_item = input("What is the new item?: ")

shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")