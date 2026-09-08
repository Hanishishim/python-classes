n = int(input("Enter your number:  "))
lastdigit = 0
odd = 0
even = 0

while n > 0:
    lastdigit = n % 10
    if lastdigit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print ({odd}, {even})