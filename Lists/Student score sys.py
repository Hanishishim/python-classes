students = {}
while True:
    print(f"""
     --------------- Student Scores ------------------

                1. Add student
                2. Remove Student
                3. Show all scores
                4. Modify Student score
                5. Exit
    --------------------------------------------------
    """)
    choice = int(input("Enter a option: "))
    if choice == 1:
        student_name = input("Enter the student's name: ")
        student_score = int(input("Enter the student's score:"))
        if student_name not in students:
            students[student_name] = student_score
            print(f"{student_name} is added successfully!")
        else: 
            print("Student already exists!")
    elif choice == 2:
        student_name = input("Enter the student's name: ")
        if student_name in students:
            del students[student_name]
            print(f"{student_name} is removed successfully!")
        else:
            print("Student not found!")
    elif choice == 3:
        max(students.values())
        min(students.values())
        print (students)
        print(f"The Highest score is {max(students.values())}")
        print(f"The Lowest score is {min(students.values())}")
    elif choice == 4:
        student_name = input("Enter the student's name: ")
        if student_name in students:
            student_new_score = int(input("Enter the student's score:"))
            students[student_name] = student_new_score
            print(f"{student_name}'s score is now {student_new_score}")
        else:
            print("Student not found!")
    elif choice == 5:
        print("Thanks for using Students Scores system!")
        print("Goodbye!")
        break






