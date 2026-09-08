math = int(input("What is your score for Math:"))
science = int(input("What is your score for Science:"))
english = int(input("What is your score for English:"))
computer = int(input("What is your score for Computer:"))
totalmarks = math + science + english + computer

if totalmarks >= 90:
    print ("Your score is A")
elif totalmarks >= 80:
    print ("Your score is B")
elif totalmarks >= 70:
    print("Your score is C")
elif totalmarks >= 60:
    print ("Your score is D")
else:
    print ("Your score is F")

