import sys

# Check the length of command-line arguments
arg_len = len(sys.argv)

# Handle case with no command provided
if arg_len == 1:
    print('\n')
    print("Usage: todo <command>")
    print('\n')
# Handle case with one argument (e.g., "add", "list", "remove", "done")
elif arg_len == 2:
    if sys.argv[1] == "add":
        print('\n')
        print("Usage: todo add <task>")
        print('\n')
    elif sys.argv[1] == "list" or sys.argv[1] == "ls":
        # Display all tasks
        try:
            with open("todoHolder.txt", "r") as file:
                tasks = file.readlines()
            tasks = [task.strip() for task in tasks if not task.startswith("!!")]  # Filter out hidden tasks
            if not tasks:
                print('\n')
                print("No tasks found.")
                print('\n')
            else:
                print('\n')
                print("To-do list:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
                print("\n")
        except FileNotFoundError:
            print('\n')
            print("No tasks found.")
            print('\n')
    elif sys.argv[1] == "remove":
        print('\n')
        print("Usage: todo remove <task_number>")
        print('\n')
    elif sys.argv[1] == "edit":
        print('\n')
        print("Usage: todo edit <task_number> <new task content>")
        print('\n')
    elif sys.argv[1] == "hide":
        print('\n')
        print("Usage: todo hide <task_number>")
        print('\n')

    elif sys.argv[1] == "unhide":
        try:
            with open("todoHolder.txt", "r") as file:
                tasks = file.readlines()
            
            updated_tasks = [task.lstrip("!!") for task in tasks]
            
            with open("todoHolder.txt", "w") as file:
                file.writelines(updated_tasks)
            
            print('\n')   
            print("All hidden tasks unhidden.")
            print('\n')
        except FileNotFoundError:
            print('\n')              
            print("No tasks found.")
            print('\n')
elif arg_len == 3:
    command = sys.argv[1]
    task_input = sys.argv[2]

    if command == "add":
        # Add a regular task without cut
        try:
            with open("todoHolder.txt", "a") as file:
                file.write(task_input + "\n")
            print('\n')
            print(f"Task added: {task_input}")
            print('\n')
        except Exception as e:
            print('\n')
            print(f"Error adding task: {e}")
            print('\n')
    elif command == "remove":
        # Remove a task using task number
        confirmation = input(f"Task, {task_input} should be deleted? Y/N: ").replace(" ","")
        if confirmation == "y" or confirmation == "Y":
            try:
                task_number = int(task_input)  # Convert input to integer
                with open("todoHolder.txt", "r") as file:
                    tasks = file.readlines()
                
                if 1 <= task_number <= len(tasks):
                    # Remove task by index (task_number - 1)
                    tasks.pop(task_number - 1)
                    # Re-write the file with the remaining tasks
                    with open("todoHolder.txt", "w") as file:
                        file.writelines(tasks)  # Use writelines to preserve line breaks
                    print('\n')   
                    print(f"Task {task_number} removed.")
                    print('\n')
                else:
                    print('\n')
                    print(f"Task number {task_number} is out of range.")
                    print('\n')
            except ValueError:
                print('\n')
                print("Please provide a valid task number.")
                print('\n')
            except FileNotFoundError:
                print('\n')
                print("No ToDoos found, add some using todo add <task>")
                print('\n')
        elif confirmation == "n" or confirmation == "N":
            print("Terminated.")
        else:
            print("No input recieved or wrong input recieved, Terminated.")
    elif command == "hide":
        # Hide a task using task number
        confirmation = input(f"Task, {task_input} should be hidden? Y/N: ").replace(" ", "")
        if confirmation.lower() == "y":
            try:
                task_number = int(task_input)  # Convert input to integer

                # Open the file and read the tasks
                with open("todoHolder.txt", "r") as file:
                    tasks = file.readlines()

                # Count the number of hidden tasks (lines starting with "!!")
                hidden_count = sum(1 for task in tasks if task.startswith("!!"))

                # Adjust the task number by subtracting the number of hidden tasks
                adjusted_task_number = task_number + hidden_count

                # Check if the task number is valid
                if 1 <= adjusted_task_number <= len(tasks):
                    task_index = adjusted_task_number - 1  # Zero-based index

                    # Ensure the task is not already hidden
                    if tasks[task_index].startswith("!!"):
                        print(f"\nTask {task_number} is already hidden.\n")
                    else:
                        # Mark the task as hidden by adding "!!" at the start
                        tasks[task_index] = "!!" + tasks[task_index]
                        with open("todoHolder.txt", "w") as file:
                            file.writelines(tasks)  # Preserve line breaks

                        print(f"\nTask {task_number} hidden.\n")
                else:
                    print(f"\nTask number {task_number} is out of range.\n")
            except ValueError:
                print("\nPlease provide a valid task number.\n")
            except FileNotFoundError:
                print("\nTodo file not found.\n")
            
# Handle case with three arguments (e.g., "edit <task_number> <new task>")
elif arg_len == 4:
    command = sys.argv[1]
    task_input = sys.argv[2]  # This should be the task number
    new_task = sys.argv[3]  # This should be the new task content

    if command == "edit":
        try:
            task_number = int(task_input)  # Convert task_input to integer (task number)
            
            # Read the current tasks from the file
            with open("todoHolder.txt", "r") as file:
                tasks = file.readlines()
            
            if 1 <= task_number <= len(tasks):
                task_index = task_number - 1  # Convert to 0-based index
                
                # If the new task contains "::", append the new content to the existing task
                if "::" in new_task:
                    task_to_edit, additional_content = new_task.split("::", 1)
                    tasks[task_index] = tasks[task_index].strip() + additional_content + "\n"
                else:
                    # Otherwise, replace the task entirely
                    tasks[task_index] = new_task + "\n"
                
                # Re-write the file with the updated tasks
                with open("todoHolder.txt", "w") as file:
                    file.writelines(tasks)

                print('\n')   
                print(f"Task {task_number} edited.")
                print('\n')
            else:
                print('\n')
                print(f"Task number {task_number} is out of range.")
                print('\n')
        except ValueError:
            print('\n')
            print("Please provide a valid task number and content.")
            print('\n')
        except FileNotFoundError:
            print('\n')
            print("No ToDoos found, add some using todo add <task>")
            print('\n')
else:
    print('\n')
    print("Too many arguments. Usage: todo <command>")
    print('\n')
