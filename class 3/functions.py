# def groot():
#     print("Hello, Good morning!")
# groot()

# def tea_maker():
#     print("taking milk")
#     print("taking tea powder")
#     print("taking spices")
#     print("Boiling them together")
#     print("Pouring the tea in a cup")
# tea_maker()
def add():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    print(f"Sum of {num1} and {num2} is {sum}")
def sub():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num1 > num2:
            sub = num1 - num2
            print(f"Difference between {num1} and {num2} is {sub}")
        else:
            print("Your first number is smaller than your second one")
def mul():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        mul = num1 * num2
        print(f"Product of {num1} and {num2} is {mul}")
def div():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        div = num1 / num2
        print(f"Quotient of {num1} and {num2} is {div}")
def rem():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    rem = num1 % num2
    print(f"Remainder of {num1} and {num2} is {rem}")

while True:
    print(f"""
    -------AI Calculator------
        1. Add numbers
        2. Subtract numbers
        3. Multipliy numbers
        4. Divide numbers
        5. Find the remainder
        6. Exit
    """)
    choice = int(input("Pick a option: "))
    if choice == 1:
        add()
    if choice == 2:
        sub()
    if choice == 3:
        mul()
    if choice == 4:
        div()
    if choice == 5:
        rem()
    if choice == 6:
         print("Thank you for using -------AI Calculator------ ")
         break
     
