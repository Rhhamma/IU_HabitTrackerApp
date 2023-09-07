from analytics import *
def main():
    """
    The main function for the Habit Tracker CLI.

    """
    habit_tracker = HabitTracker()
    habit_tracker.load_from_file("habit_data.json")

    while True:
        print("Habit Tracker Menu:")
        print("1. Create a habit")
        print("2. Complete a task")
        print("3. Delete a habit")
        print("4. List all habits")
        print("5. List habits by periodicity")
        print("6. Get longest streak for a habit")
        print("7. Get longest streak for all habits")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_habit(habit_tracker)
        elif choice == "2":
            complete_task(habit_tracker)
        elif choice == "3":
            delete_habit_menu(habit_tracker)
        elif choice == "4":
            list_all_habits(habit_tracker)
        elif choice == "5":
            list_habits_by_periodicity(habit_tracker)
        elif choice == "6":
            get_longest_streak_for_habit(habit_tracker)
        elif choice == "7":
            get_longest_streak_for_all_habits(habit_tracker)
        elif choice == "0":
            habit_tracker.save_to_file("habit_data.json")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
