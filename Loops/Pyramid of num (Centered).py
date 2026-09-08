n = int(input("Enter a number: "))
for j in range (n):
    print (" " * (n-j), end=" ")
    for i in range (j+1):
        print (i+1, end=" ")
        
    print (end="\n")

