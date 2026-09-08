n = int(input("Enter your number: "))
lastdigit = 0
mul = 1
sum = 0

while n > 0:
    lastdigit = n % 10
    mul = mul * lastdigit
    n = n // 10
print (f" The product of the digits is {mul}")