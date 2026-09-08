n = int(input("Enter a number: "))
lastdigit = 0
rev = 0

while n > 0:
    lastdigit = n % 10
    rev = rev * 10 + lastdigit
    n = n // 10
print (rev)