print("Enter a list of numbers, type 0 when finished.")
numbers = []
new_number = 1
sum_total =  0

# or
#largest = 0

while new_number != 0:
    try:
        new_number = float(input("Enter number: "))

        if new_number != 0:
            numbers.append(new_number)
    except ValueError:
        print("Invalid input. Please enter a valid input")

for value in numbers:
    sum_total += value
    average = sum_total / len(numbers)
    maximum_number = max(numbers)

    # or
    #if value > largest:
       #largest = value 

print(f"The sum is: {sum_total}")
print(f"The average is: {average}")
print(f"The largest number is: {maximum_number}")

# or
#print(f"The largest number is: {largest}")

positive_numbers = [value for value in numbers if value > 0]

## Find the smallest positive number
smallest_positive = min(positive_numbers, default=None)

##Print the result
if smallest_positive is None:
    print("No positive numbers were entered.")
else:
    print("The smallest positive number is:", smallest_positive)

# or 

# #minimum_number = 999999999999999
# for value in numbers:
    
#     if value > 0 and value < minimum_number:
#         minimum_number = value
       
            
# print(f"The smallest positive number is: {minimum_number}") 

# sorted list
sorted_list = sorted(numbers)
print("The sorted List is: ")
for value in sorted_list:
    print(value)



       


