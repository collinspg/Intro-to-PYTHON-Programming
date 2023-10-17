grade = int(input('Please enter your grade percentage: '))

if grade >= 90:
    letter_grade = 'A'

elif grade >= 80:
    letter_grade = 'B'

elif grade >= 70:
    letter_grade = 'C'

elif grade >= 60:
    letter_grade = 'D'

else:
    letter_grade ='F'
#print(f'Your grade is: {letter_grade}')

#if grade >= 70:
    #print('Congratulations you passed the class.')
#else:
    #print('Sorry, you did not meet the requirement to pass this class. Please try harder.')

#stretch 1

sign = ''
last_digit = grade % 10

if last_digit >= 7:
    sign = '+'
elif last_digit < 3:
    sign = '-'
else:
    sign = ''

# stretch 2
if grade >= 93:
    sign = ''

# stretch 3
if letter_grade == 'F':
    sign = ''

print(f'Your grade is: {letter_grade}{sign}')
if grade >= 70:
    print('Congratulations you passed the class.')
else:
    print('Sorry, you did not meet the requirement to pass this class. Please try harder.')