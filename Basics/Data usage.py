datauseage = float(input("Enter your data usage:"))
primeuser = input("Are you a prime user?")
baseprice = 300
dicount = 0
totalamount = baseprice

if datauseage > 5:
    totalamount = totalamount + 50

if primeuser == "yes":
    dicount = totalamount * (10/100)
    totalamount = totalamount - dicount

print(f"""

        Base price: {baseprice}
        Discount: {dicount}
        Final price: {totalamount}


""")