Student_Attendance = [] 

while True: 
    print("""
    ----------- Student Attendance System ----------- 
    1. Mark Student Present 
    2. Remove Student 
    3. Show Attendance List 
    4. Modify Student Attendance
    5. Exit 
    -------------------------------------------------- 
    """)
    
    choice = input("Enter option (1-5): ").strip()
    
    if choice == "1": 
        student_info = {} 
        student_name = input("Enter the student's name: ").strip()
        titles = [x['title'] for x in Student_Attendance] 
        
        if student_name not in titles: 
            presentORnot = input(f"Is the student {student_name} present or not? ").strip()
            student_info['title'] = student_name 
            student_info['att'] = presentORnot 
            Student_Attendance.append(student_info) 
            print(f"\n--------Student Marked {presentORnot}--------") 
            print("Name: ", student_name) 
            print("Attendance: ", presentORnot) 
        else: 
            print("Student already exists!") 

    elif choice == "2": 
        remove_student = input("Enter student's name: ").strip()
        titles = [x['title'] for x in Student_Attendance] 
        
        if remove_student in titles: 
            for student in Student_Attendance:
                if student['title'] == remove_student:
                    Student_Attendance.remove(student)
                    break
            print("----Student removed!----") 
        else: 
            print("Student not found!") 

    elif choice == "3": 
        if len(Student_Attendance) == 0: 
            print("Your Attendance list is empty!") 
        else: 
            print("Your Attendance list:") 
            for item in Student_Attendance: 
                print(f"Name: {item['title']} | Attendance: {item['att']}") 

    elif choice == "4": 
        change = input("Enter the student's name: ").strip()
        titles = [x['title'] for x in Student_Attendance] 
        
        if change in titles: 
            changeATT = input("What is the student's new attendance status?: ").strip()
            for student in Student_Attendance:
                if student['title'] == change: 
                    student['att'] = changeATT 
            print(f"Student {change} is marked {changeATT}") 
        else:
            print("Student not found!")

    elif choice == "5": 
        print("Thank you for using Student Attendance System!") 
        print("Goodbye!") 
        break
        
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
