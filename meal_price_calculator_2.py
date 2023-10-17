price_child_meal = float(input("What is the price of a child's meal? "))
price_adult_meal = float(input("What is the price of an adult's meal? "))
number_children = int(input("How many children are there? "))
number_adult = int(input("How many adults are there? "))

# Creativity and exceeding requirements. I'm adding drink to the meal price calculator
price_drink = float(input("What is the price of a drink? "))
number_of_drinks = int(input("Total number of adults and children: "))
#End of creativity and exceeding requirements

subtotal = (price_child_meal * number_children) + (price_adult_meal * number_adult) + (price_drink * number_of_drinks)
print(f"\nsubtotal: ${subtotal:.2f} \n")

tax_rate = float(input("What is the sales tax rate? "))
sales_tax_rate = (subtotal * tax_rate) / 100
total = subtotal + sales_tax_rate
print(f"sales tax: ${sales_tax_rate:.2f}")
print(f"Total: ${total:.2f} \n")

pay_amount = float(input("What is the payment amount? "))
change = pay_amount - total
print(f"Change: ${change:.2f} \n")