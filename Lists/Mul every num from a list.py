numbers = [5,10,15,20,25,30,35,40,45,50]
print(numbers)
x = len(numbers)
i = 0
while i < x:
    j = numbers[i]
    j = j * 2
    numbers[i] = j
    i = i + 1
print(numbers)
