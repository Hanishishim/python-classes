num = int(input("Enter your number:"))
remainderby2 = num % 2
remainderby3 = num % 3
remainderby5 = num % 5
remainderby10 = num % 10
if (remainderby2 == 0 and remainderby3 == 0 or remainderby5 == 0 and remainderby10 == 0):
    print ("Your number is divisible by 2,3 or 5,10")
else:
    print ("Your number is not divisible by 2,3 or 5,10")