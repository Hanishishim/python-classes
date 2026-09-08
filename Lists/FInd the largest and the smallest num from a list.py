ages = [11,45,33,67,24,46,76,16,28]
x = len(ages)
i = 0
largest_num = 0
smallest_num = ages[0]
while i < x:
    j = ages[i]
    if j > largest_num:
        largest_num = j
    if j < smallest_num:
        smallest_num = j
    i = i + 1
print (f"""
    largest number: {largest_num}
    smallest number: {smallest_num}
""")