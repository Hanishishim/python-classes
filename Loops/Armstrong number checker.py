n = int(input("Enter a number:"))
og = n
on = n
count = 0
rem = 0
sum = 0

while n > 0:
    count = count + 1
    n = n // 10
while og > 0:
    rem = og % 10
    sum = sum + rem**count
    og = og // 10
if sum == on: 
    print("Armstrong number ")
else:
    print ("Not an Armstrong number ")
