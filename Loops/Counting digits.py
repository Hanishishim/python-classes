n = int(input("Enter a number: "))
count = 0

while n > 0:
    count = count + 1
    n = n // 10

print (f"total count is {count}")

n = int(input("Enter a number: "))
count = 0
add = 0
rem = 0
while n > 0:
    rem = n % 10
    add = add + rem
    n = n // 10 
print(f"total sum is {add}")

