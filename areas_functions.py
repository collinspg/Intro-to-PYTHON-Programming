import math

#This function calculates the area of a square and returns the value to the user
def compute_area_square(side):
    return side * side

#This function calculates the area of a rectangle and returns the value to the user
def compute_area_rectangle(length, width):
    return length * width

#This function calculates the area of a circle and returns the value to the user
def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ""

while True:

    shape = input("What shape do you have? ")
    
    if shape.lower() == "square":
        side = float(input("What is the length of the side? "))
        area_of_square = compute_area_square(side)
        print(f"The area of the square is {area_of_square:.2f}")

    elif shape.lower() == "rectangle":
        length = float(input("What is the length of the rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        area_of_rectangle = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is {area_of_rectangle:.2f}")

    elif shape.lower() == "circle":
        radius = float(input("What is the radius of the circle? "))
        area_of_circle = compute_area_circle(radius)
        print(f"The area of the circle is {area_of_circle:.2f}")

    elif shape.lower() == "quit":
        break

    else:
        print("Invalid shape! Please enter a valid shape: 'SQUARE', 'RECTANGLE', OR 'CIRCLE'")
