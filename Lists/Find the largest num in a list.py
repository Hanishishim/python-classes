ages = [11,45,33,67,24,46,76,16,28]
largest_num = 0
x = len(ages)
i = 0
while i < x:
    j = ages[i]
    if j > largest_num:
        largest_num = j
    i = i + 1
print (largest_num)