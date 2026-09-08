ages = [11,45,33,67,24,46,76,16,28]
x = len(ages)
i = 0
while i < x:
    j = (ages[i])
    if j % 2 == 0:
        ages[i] = ages[i] * 10
    else:
        ages[i] = ages[i] + 10
    i = i + 1
print (ages)

for i in range (len(ages)):
    if ages[i] % 2 == 0:
        ages[i] = ages[i] * 10
    else:
        ages[i] = ages[i] + 10
print (ages)
        