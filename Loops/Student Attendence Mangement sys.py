Student_Attendance = []

while True:
    print(f"""
    ----------- Student Attendance System -----------

                1. Mark Student Present
                2. Remove Student
                3. Show Attendance List
                4. Modify Student Name
                5. Exit
    --------------------------------------------------
    """)
    choice = int(input("Choose a option: "))
    if choice == 1:
        student_name = input("Enter a Student's Name: ")
        if student_name not in Student_Attendance:
            Student_Attendance.append(student_name)
            print(f"{student_name} is marked present!")
        else:
            print(f"{student_name} is already added!")
    elif choice == 2:
        student_name = input("Enter a Student's Name ")
        if student_name in Student_Attendance:
            Student_Attendance.remove(student_name)
            print(f"{student_name} is removed!")
        else:
            print(f"{student_name} is not found!")
    elif choice == 3:
        elements = len(Student_Attendance)
        if elements > 0:
            print(Student_Attendance)
        else:
            print("The list is empty")
    elif choice == 4:
        student_name = input("Enter a Student's Name ")
        if student_name in Student_Attendance:
            new_student_name = input("Enter a New Student's Name: ")
            index_num = Student_Attendance.index(student_name)  
            Student_Attendance[index_num] = new_student_name         
            print(f"Changed '{student_name}' to '{new_student_name}'")
        else:
            print('"Student not found!')
    elif choice == 5:
        print("Thank you for using Student Attendance System!")
        print("Goodbye!")
        break









