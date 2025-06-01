# daily_reminder.py

def main():
    while True:
        task = input("Enter your task: ").strip()
        priority = input("Priority (high/medium/low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

        match priority:
            case "high":
                message = f"'{task}' is a high priority task"
            case "medium":
                message = f"'{task}' is a medium priority task"
            case "low":
                message = f"'{task}' is a low priority task"
            case _:
                print("Invalid priority entered. Please enter high, medium, or low.")
                continue

        if time_bound == "yes":
            message += " that requires immediate attention today!"
        elif time_bound == "no":
            message += ". Consider completing it when you have free time."
        else:
            print("Invalid input for time-bound. Please enter yes or no.")
            continue

        print("\nReminder:", message)
        break

if __name__ == "__main__":
    main()
