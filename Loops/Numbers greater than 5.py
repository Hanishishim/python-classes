n = int(input("Enter a number: "))
lastdigit = 0
digitsgreaterthan5 = 0
digitslessthan5 = 0

while n > 0:
    lastdigit = n % 10
    if lastdigit > 5:
        digitsgreaterthan5 = digitsgreaterthan5 + 1
    else: 
        digitslessthan5 = digitslessthan5 + 1
    n = n // 10
print (f" Digits greater than 5 is {digitsgreaterthan5} and digit less than 5 is {digitslessthan5}")
    

