task = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

if task and priority and time_bound:
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"'{task}' is a high priority task that requires immediate attention today!")
            elif time_bound == "no":
                print(f"'{task}' is a high priority task. Consider completing it when you have free time.")
        case "medium":
            if time_bound == "yes":
                print(f"'{task}' is a medium priority task that requires immediate attention today!")
            elif time_bound == "no":
                print(f"'{task}' is a medium priority task. Consider completing it when you have free time.")
        case "low":
            if time_bound == "yes":
                print(f"'{task}' is a low priority task that requires immediate attention today!")
            elif time_bound == "no":
                print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
else:
    print("Some fields are missing inputs. Please try again later!")