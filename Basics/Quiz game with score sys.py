welcome = print ("Welcome to your quiz on math. This will have 5 questions, with each worth 10 points. You may begin now. Hope you studied, and are prepared. ALL THE BEST!")
score = 0
question_1 = int(input("What is 64/16:"))
question_2 = int(input("What is 5+7:"))
question_3 = int(input("What is 24 - 8:"))
question_4 = int(input("What is 6 * 7:"))
question_5 = int(input ("What is 24/8 * 7:"))

if question_1 == 4:
    finalscore = score + 10 

if question_2 == 12:
    finalscore = finalscore + 10

if question_3 == 16:
    finalscore = finalscore + 10

if question_4 == 42:
    finalscore = finalscore + 10

if question_5 == 21:
    finalscore = finalscore + 10

totalscore = finalscore

if totalscore == 50:
    print("Excellent")
elif totalscore >= 30 and totalscore <= 40: 
    print ("Good job")
else: 
    print ("Practice more")

