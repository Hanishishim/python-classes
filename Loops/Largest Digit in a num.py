n = int(input("Enter a number: "))
lastdigit = 0
largestdigit = 0
smallestdigit = 0

while n > 0:
    lastdigit = n % 10
    if largestdigit < lastdigit:
            largestdigit = lastdigit
    else:
        if largestdigit > lastdigit:
            smallestdigit = lastdigit
    n = n // 10
print (f" Largest digit is {largestdigit}")


n = int(input("Enter a number: "))
largestdigit = 0
while n > 0:
    lastdigit = n % 10
    if lastdigit > largestdigit:
        largestdigit = lastdigit
    n = n // 10
print (largestdigit)

