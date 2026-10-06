# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# try:
#     divResult = x/y
#     print(divResult)

# except Exception as e:
#     print("some error ocurred: ", e)
#     y = 1
#     divResult = x/y
#     print("error handled, y=0, we set it as 1")
# print("HI HANISH!")

# ex 2 Value Error
# try:
#     num = int(input("Enter a number: "))
#     print(f"this is a num,{num}")

# except Exception as e:
#     print("some error occured", e)

# def takeUnput():
#     x = int(input("Enter: "))
#     y = int(input("Enter: "))
#     return(x,y)
# try:
#     x,y = takeUnput()
#     div = x/y
#     print(div)
# except ValueError as e:
#     print("error", e)
#     x,y = takeUnput()
#     div = x/y
#     print(div)
# except ZeroDivisionError as e:
#     print("error", e)
#     y = int(input("Enter for y"))
#     div = x/y
# except Exception as e:
#     print("Error", e)
    
