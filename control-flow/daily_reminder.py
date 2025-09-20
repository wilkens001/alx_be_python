task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

print()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Plan to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Schedule it accordingly.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task to complete today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")