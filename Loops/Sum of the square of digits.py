n = int(input("Enter your number:  "))
sqr = 0
sum = 0
rem = 0

while n > 0:
    rem = n % 10
    sqr = rem ** 2
    sum = sum + sqr
    n = n // 10
print (f" sum of the squares of the digits is {sum}")