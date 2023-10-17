#Core requirements
length_of_a_square = float(input('What is the length of a side of the square? '))
area_of_a_square = length_of_a_square ** 2
print(f'The area of the square is: {area_of_a_square} \n') 

length_of_a_rectangle = float(input('What is the length of rectangle? '))
width_of_a_rectangle = float(input('What is the width of the rectangle? '))
area_of_a_rectangle = length_of_a_rectangle * width_of_a_rectangle
print(f'The area of the rectangle is: {area_of_a_rectangle} \n')

radius = float(input('What is the radius of the circle? '))
area_of_a_circle = 3.14 * (radius ** 2)
print(f'The area of the circle is: {area_of_a_circle:.1f} \n')

#Stretch1 math library
import math
radius = float(input('What is the radius of the circle? '))
area_of_a_circle = math.pi * (radius ** 2)
print(f'The area of the circle is: {area_of_a_circle:.1f} \n')

#Stretch2 include volumes
value = float(input('Please enter a value to be used \n') )
#areas
area_of_a_square = value ** 2
area_cirle = math.pi * (value ** 2)
volume_of_a_cube = value ** 3
volume_of_a_sphere = 4/3 * math.pi * (value ** 3) 

#results
print(f'Area of a Square: {area_of_a_square:.1f}')
print(f'Area of a Circle: {area_cirle:.1f}')
print(f'Volume of a Cube: {volume_of_a_cube:.1f}')
print(f'Volume of a Sphere: {volume_of_a_sphere:.1f} \n')

#Stretch3 core assignments in cm 
length_of_a_square = float(input('What is the length of a side of the square?(in cm) '))
area_of_a_square = length_of_a_square ** 2
print(f'The area of the square is: {area_of_a_square:.1f} cm^2') 
print(f'The area of the square is: {area_of_a_square / 10000 :.1f} m^2 \n') 

length_of_a_rectangle = float(input('What is the length of rectangle?(in cm) '))
width_of_a_rectangle = float(input('What is the width of the rectangle? '))
area_of_a_rectangle = length_of_a_rectangle * width_of_a_rectangle
print(f'The area of the rectangle is: {area_of_a_rectangle:.1f} cm^2 ')
print(f'The area of the rectangle is: {area_of_a_rectangle / 10000 :.1f} m^2 \n')

radius = float(input('What is the radius of the circle?(in cm) '))
area_of_a_circle = 3.14 * (radius ** 2)
print(f'The area of the circle is: {area_of_a_circle:.1f} cm^2')
print(f'The area of the circle is: {area_of_a_circle / 10000 :.1f} m^2 ')



