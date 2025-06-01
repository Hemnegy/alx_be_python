# daily_reminder.py

def main():
    while True:
        task = input("Enter your task: ").strip()
        priority = input("Priority (high/medium/low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

        if priority == "high":
            message = f"'{task}' is a high priority task"
        elif priority == "medium":
            message = f"'{task}' is a medium priority task"
        elif priority == "low":
            message = f"'{task}' is a low priority task"
        else:
            print("Invalid priority entered. Please enter high, medium, or low.")
            continue  # Ask again

        if time_bound == "yes":
            message += " that requires immediate attention today!"
        elif time_bound == "no":
            message += ". Consider completing it when you have free time."
        else:
            print("Invalid input for time-bound. Please enter yes or no.")
            continue  # Ask again

        print("\nReminder:", message)
        break

if __name__ == "__main__":
    main()
