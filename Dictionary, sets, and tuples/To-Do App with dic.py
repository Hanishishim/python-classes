# 1. Initialize todolist as a list to store task dictionaries
todolist = [] 

while True:
    print("""
    ------------ TO-DO APP ------------
    1. Add Task
    2. Remove Task
    3. Show All Tasks
    4. Modify Task
    5. Exit
    -----------------------------------
    """)
    
    # 2. Keep choice as a string to avoid crashes if someone types a letter
    choice = input("Enter option (1-5): ").strip() 
    
    # --- 1. ADD TASK ---
    if choice == "1":
        task_name = input("What task do you wanna add: ").strip()
        
        # Check if the task title already exists in our list
        already_exists = False
        for existing_task in todolist:
            if existing_task['title'].lower() == task_name.lower():
                already_exists = True
                break
                
        if already_exists:
            print("Task is already added!")
        else:
            description = input("Enter description: ")
            deadline = input("Enter a deadline for this task: ")
            priority = input("Enter priority: ")
            status = False  # Python boolean must be capitalized (False, not false)
            
            # Create the dictionary and append it to the list
            task = {
                'title': task_name,
                'description': description,
                'deadline': deadline,
                'priority': priority,
                'status': status
            }
            todolist.append(task)
            print(f"Task '{task_name}' added successfully!")

    # --- 2. REMOVE TASK ---
    elif choice == "2":
        if not todolist:
            print("Your to-do list is empty.")
        else:
            task_to_remove = input("Enter the title of the task to remove: ").strip()
            found = False
            for task in todolist:
                if task['title'].lower() == task_to_remove.lower():
                    todolist.remove(task)
                    print(f"Task '{task['title']}' removed successfully!")
                    found = True
                    break
            if not found:
                print("Task not found.")

    # --- 3. SHOW ALL TASKS ---
    elif choice == "3":
        if not todolist:
            print("No tasks found!")
        else:
            print("\n=== CURRENT TASKS ===")
            for index, task in enumerate(todolist, 1):
                status_text = "Completed" if task['status'] else "Pending"
                print(f"{index}. Title: {task['title']}")
                print(f"   Description: {task['description']}")
                print(f"   Deadline: {task['deadline']} | Priority: {task['priority']} | Status: {status_text}")
                print("-" * 30)

    # --- 4. MODIFY TASK ---
    elif choice == "4":
        if not todolist:
            print("No tasks to modify.")
        else:
            task_to_modify = input("Enter the title of the task you want to modify: ").strip()
            found = False
            for task in todolist:
                if task['title'].lower() == task_to_modify.lower():
                    found = True
                    print(f"\nModifying task: {task['title']}")
                    print("Leave field blank to keep current value.")
                    
                    new_title = input(f"New Title [{task['title']}]: ").strip()
                    new_desc = input(f"New Description [{task['description']}]: ").strip()
                    new_dead = input(f"New Deadline [{task['deadline']}]: ").strip()
                    new_prior = input(f"New Priority [{task['priority']}]: ").strip()
                    new_status = input(f"Is it completed? (y/n) [{ 'y' if task['status'] else 'n' }]: ").strip().lower()
                    
                    # Update fields only if user typed something
                    if new_title: task['title'] = new_title
                    if new_desc: task['description'] = new_desc
                    if new_dead: task['deadline'] = new_dead
                    if new_prior: task['priority'] = new_prior
                    if new_status: task['status'] = True if new_status == 'y' else False
                    
                    print("Task updated successfully!")
                    break
            if not found:
                print("Task not found.")

    # --- 5. EXIT ---
    elif choice == "5":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice, please select an option between 1 and 5.")
