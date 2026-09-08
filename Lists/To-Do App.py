tasks = []

while True:
    print(f"""
    -------TO DO APP------
        1. Add Task
        2. Remove Task
        3. Show Tasks
        4. Modify Task
        5. Exit
    """)
    
    choice = int(input("Pick a option: "))

    if choice == 1:
        task = str(input("Enter a task to add: "))
        if task not in tasks:
            tasks.append(task)
            print(f"'{task}' is added to the list")
        else:
            print("Task already exists!") 
    elif choice == 2:
        i = str(input("Enter a task to remove: "))
        if i in tasks:
            tasks.remove(i)
            print(f"'{i}' was successfully removed.")
        else:
            print("Task not found!")     
    elif choice == 3:
        print("Your current tasks:", tasks) 
    elif choice == 4:
        old_task = input("Enter what task you want to change: ")
        if old_task in tasks:
            new_task = input("Enter the new task: ")
            index_num = tasks.index(old_task)  
            tasks[index_num] = new_task         
            print(f"Changed '{old_task}' to '{new_task}'")
        else:
            print("Task not found!")
    elif choice == 5:
        print("Goodbye!")
        break
        
