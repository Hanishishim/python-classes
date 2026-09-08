n = int(input("Enter a number: "))
#x = 1
#for i in range (n):
    #for j in range (i+1):
        #print (x ,end=" ")
        #x = x + 1
    #print (end = "\n")

i = 0
x = 1
while i < n:
    j = 0
    while j < i + 1:
        print (x ,end=" ")
        x = x + 1
        j = j + 1
    print (end = "\n")
    i = i + 1

