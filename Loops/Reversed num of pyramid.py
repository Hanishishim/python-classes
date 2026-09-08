n = int(input("Enter a number:"))
for j in range (n):
    x = n
    for i in range (j+1):
        print(x, end=" ")
        x = x -1
    print(end="\n")
