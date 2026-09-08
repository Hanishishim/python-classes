ages = [11,45,33,67,24,46,76,16,28]
x = len(ages)
i = 0
even = 0
odd = 0
while i < x:
    j = ages[i]
    if j % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    i = i + 1
print({even},{odd})