# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate the reminder using match-case and conditional logic
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority"

# Adjust the message if the task is time-sensitive
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"
elif priority in ["high", "medium", "low"]:
    message += ". Consider completing it when you have free time."

# Output the final message
print("\n" + message)
