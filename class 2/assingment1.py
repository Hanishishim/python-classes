import random
x = random.randint(1,100)
while True:
    guess = int(input("Enter u're guess: "))
    if guess == x:
        print("You nailed it")
        break
    elif guess > x:
        print("Too high!")
    elif guess < x:
        print("Too low!")


50
# names = [1,2,3,4,5,6,7,8,9,10]
# print(random.choice(names))