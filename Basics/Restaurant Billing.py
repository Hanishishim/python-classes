foodtotal = float(input("What's your total bill?:"))
membership = input("Are you a member?:")
servicecharge = 0
memberdiscount = (5/100)
totalamount = foodtotal

servicecharge = foodtotal * (5/100)
foodtotalaftercharge = foodtotal + servicecharge

if membership == "yes": 
    memberdiscount = foodtotalaftercharge * (5/100)
    foodtotalaftercharge = foodtotalaftercharge - memberdiscount

print (f"""

        Total food = {foodtotal}
        Service Charge = {servicecharge}
        Membership Dicount = {memberdiscount}
        Final amount = {foodtotalaftercharge}

""")

