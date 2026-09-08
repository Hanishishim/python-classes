purchaseAmount = float(input("Enter purchase amount: "))
couponCode = input("Enter coupon: ")
finalAMount  = purchaseAmount

discountOn500 = 0
discountCoupon = 0
validCoupon = "SAVE10"

if purchaseAmount > 500:
      discountOn500 = purchaseAmount * (5/100)
      finalAMount = purchaseAmount - discountOn500
      
if couponCode == validCoupon:
     discountCoupon = 50
     finalAMount = finalAMount -discountCoupon
     
print(f"""
     
     Purchase Amount: {purchaseAmount}
     Discount for the right code: {discountOn500}
     Discount of the coupon: {discountCoupon}
     Final Amoutn: {finalAMount}

""")


