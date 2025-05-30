# daily_reminder.py
# A simple task reminder script that uses conditional statements, Match Case, and loops

def main():
    print("Welcome to your Daily Task Reminder!")
    print("Let's set up your priority task for today.\n")
    
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Validate priority input
    while priority not in ['high', 'medium', 'low']:
        print("Invalid priority level. Please enter high, medium, or low.")
        priority = input("Priority (high/medium/low): ").lower()
    
    # Validate time-bound input
    while time_bound not in ['yes', 'no']:
        print("Please answer with yes or no.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    print("\nReminder: ", end='')
    
    # Process task based on priority using match case
    if priority == 'high':
        if time_bound == 'yes':
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. You should focus on this soon.")
    
    elif priority == 'medium':
        if time_bound == 'yes':
            print(f"'{task}' is a medium priority task with a deadline. Try to complete it today.")
        else:
            print(f"'{task}' is a medium priority task. Schedule time for it this week.")
    
    elif priority == 'low':
        if time_bound == 'yes':
            print(f"'{task}' is a low priority task but has a deadline. Complete it when possible.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("\n🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()