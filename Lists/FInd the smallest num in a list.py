ages = [11,45,33,67,24,46,76,16,28]
num = ages[0]
x = len(ages)
i = 0
while i < x:
    j = ages[i]
    if j < num:
        num = j
    i = i + 1
print (num)