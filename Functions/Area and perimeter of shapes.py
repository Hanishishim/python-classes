import math
def calculateRectangleArea(height,width):
    area = height*width
    print(f"""Area of rectangle with hieght 
    {height} and width of {width} is {area}""")

def calculateRectanglePerimeter(height,width):
    perimeter = (height+width) * 2
    print(f"""Perimeter of rectangle with hieght 
    {height} and width of {width} is {perimeter}
    """)

def calculateCircleArea(radius):
    area = math.pi * (radius**2)
    print(f"""Area of circle with radius being  
        {radius} is {area}""")
    
def calculateCircleperimeter(radius):
    perimeter = (math.pi * radius) * 2
    print(f"""Perimeter of circle with radius being 
        {radius} is {perimeter}
        """)
def calculateTriangleArea(base,height):
    area = (base*height) / 2
    print(f"""Area of Triangle with hieght 
        {height} and base of {base} is {area}""")
def calculateTriangleperimeter(side1,side2,side3):
    perimeter = side1 + side2 + side3
    print(f"""Perimeter of Triangle with side #1 being  
        {side1} side #2 being {side2} and side #3 being {side3} is 
        {perimeter}""")
while True:
    print(f"""
    -------AI Calculator------
        1. Find rectangles area
        2. Find rectangles perimeter
        3. Find circles area
        4. Find circle perimeter
        5. Find triangle area
        6. Find triangle perimeter
        7. Exit
    """)
    choice = int(input("Pick a option: "))
    if choice == 1:
        height = int(input("Enter the height of the rectangle"))
        width = int(input("Enter the width of the rectangle"))
        calculateRectangleArea(height = height,width = width)
    elif choice == 2:
        height = int(input("Enter the height of the rectangle"))
        width = int(input("Enter the width of the rectangle"))
        calculateRectangleArea(height = height,width = width)
    elif choice == 3:
         radius = int(input("Enter the radius of the circle"))
         calculateCircleArea(radius = radius)
    elif choice == 4:
        radius = int(input("Enter the radius of the circle"))
        calculateCircleArea(radius = radius)
    elif choice == 5:
        height = int(input("Enter the height of the rectangle"))
        width = int(input("Enter the width of the rectangle"))
        calculateRectangleArea(height = height,width = width)    
    elif choice == 6:
        Side1 = int(input("Enter the base length of the rectangle"))
        Side2 = int(input("Enter the side length of the rectangle"))
        Side3 = int(input("Enter the other side length of the rectangle"))
        calculateTriangleperimeter(Side1,Side2,Side3)
    elif choice == 7:
        print("Thank you for using -------AI Calculator------ ")
        break






