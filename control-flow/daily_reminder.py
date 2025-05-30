# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate the reminder using match-case-like logic
if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
elif priority == "medium":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
elif priority == "low":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
else:
    print(f"'{task}' has an unknown priority.")
