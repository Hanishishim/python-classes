#tuple = immutable
#list = mutable
t = ((1,2,3),(3,4,5))
t2 = ((12,25,32),(3,94,5))
list = []
for i in range(len(t)):
    list.append([])

for i in range(2):
    for j in range (3):
        element = t[i][j]
        element2 = t2[i][j]
        sum = (element + element2)
        list[i].append(sum)
print (list)




