units = float(input("How many units did you use?:"))
surcharge = 0
bet_0_100 = 0
bet_101_300 = 0
bet_300_ = 0
if units <= 100:
    bet_0_100 = units * 5
elif units >100 and  units<=300:
    bet_0_100 = 100*5  
    bet_101_300 = (units-100) * 7
elif units > 300:
    bet_0_100 = 100 * 5 
    bet_101_300 = 200*7 
    bet_300_ = (units - 300)*10
 
bill = bet_0_100 + bet_101_300 + bet_300_
if bill > 1500:
    surcharge = bill * (8/100)
    
bill +=surcharge
    
    
print (f"""
        units consumption:               {units}
        Calculation Bet 0 -100:          {bet_0_100}
        Calculation Bet 100 -300:        {bet_101_300}
        Calculation for 300+ :           {bet_300_}
        Surcharge =                      {surcharge}
        Final Bill:                      {bill}
""")
