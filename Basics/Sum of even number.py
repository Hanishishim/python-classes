#n = int(input("Enter your number: "))
#sum = 0
#rem = 0
#for i in range (0,n+1):
    #rem = i % 2
    #if rem == 0:
        #sum = sum + i
#print (f" {sum} ")
#print ("while")
#i = 0
#sum = 0
#while i <= n:
   # rem = i % 2
    #if rem == 0:
        #sum = sum + i
    #i = i + 1
#print (f" {sum} ")

n = int(input("Enter your number: "))
sum = 0
div = 0
sqr = 0
for i in range (0,n,1):
    div = i % 3
    if div == 0:
        sqr = i ** 2
        sum = sum + sqr
print (f"{sum}")
print ("while")
i = 0
sqr = 0
sum = 0
while i <= n:
    div = i % 3
    if div == 0:
        sqr = i ** 2
        sum = sum + sqr
    i = i + 1
print (f" {sum} ")