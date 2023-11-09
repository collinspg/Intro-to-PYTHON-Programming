# numbers = []

# while True:
#     num = float(input("Enter a number (enter 0 to stop): "))
#     if num == 0:
#         break
#     numbers.append(num)

# # Filter positive numbers
# positive_numbers = [num for num in numbers if num > 0]

# # Find the smallest positive number
# smallest_positive = min(positive_numbers, default=None)

# # Print the result
# if smallest_positive is None:
#     print("No positive numbers were entered.")
# else:
#     print("Smallest positive number:", smallest_positive)
def fullname(w1,w2):
  return w1 + ' ' + w2

f=fullname(w2='faith',w1='charity')
print(f)
