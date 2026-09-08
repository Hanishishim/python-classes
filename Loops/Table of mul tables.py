startingnumber = int(input("Enter a starting number:"))
endingnumber = int(input("Enter a ending number: "))

for i in range (startingnumber,endingnumber):
    print(f"Mulitiplaction Table Of {i}")
    for j in range (1,11):
        print (f" {i} x {j} = {i*j}")
