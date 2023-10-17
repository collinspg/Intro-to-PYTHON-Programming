first_num = int(input('What is the first number?'))
second_num = int(input('What is the second number?'))

if first_num > second_num:
    print('The first number is greater')
else:
    print('The first number is not greater".')

if first_num == second_num:
    print('The numbers are equal')
else: 
    print('The numbers are not equal')

if second_num > first_num:
    print('The second number is greater')
else:
    print('The second number is not greater')

print()

favourite_animal = input('What is your favourite animal?')
if favourite_animal.lower() == 'duck':
    #I will beb using the double quotes for the print statements because I've a single
    #quote to the sentence
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')