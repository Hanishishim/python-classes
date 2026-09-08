cart = ["mac","photo_frame","legos","phone","drone","ps5"]
print(cart)
for i in range(3):
    x = (input("What do u want to remove: "))
    cart.remove(x)
    print(cart)