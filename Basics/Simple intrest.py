principal = int(input("Enter the principal :"))
rate = int(input ("Enter the rate:"))
year = int(input("Enter years:"))
simpleintrest = (principal * rate * year / 100)
print (f"""       
       Principal = {principal}
       Rate = {rate}
       Years = {year}

       total = {simpleintrest + principal}
       Simple intrest = {simpleintrest}
       
    

""")