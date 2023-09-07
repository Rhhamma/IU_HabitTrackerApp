from habit_tracker import Habit, HabitTracker
from datetime import datetime


def create_habit(habit_tracker):
    """
    Creates a new habit and adds it to the habit tracker.

    Args:
        habit_tracker (HabitTracker): The habit tracker instance.

    """
    name = input("Enter the habit name: ")
    periodicity = input("Enter the habit periodicity (daily/weekly): ")
    created_date = input("Enter the habit creation date (YYYY-MM-DD): ")
    habit = Habit(name, periodicity, datetime.fromisoformat(created_date).date())
    habit_names = [h.name for h in habit_tracker.habits]
    if habit.name in habit_names:
        print("Error:", habit.name, "habit exists!")
    else:
        habit_tracker.add_habit(habit)
        print(habit.name, "habit created successfully.")
        habit_tracker.save_to_file("habit_data.json")


def complete_task(habit_tracker):
    """
    Marks a task as completed for a specific habit.

    Args:
        habit_tracker (HabitTracker): The habit tracker instance.

    """
    habit_name = input("Enter the habit name: ")
    habit = find_habit_by_name(habit_tracker, habit_name)
    if habit:
        date = input("Enter the completion date (YYYY-MM-DD): ")
        habit.complete_task(datetime.fromisoformat(date).date())
        print("Task completed successfully.")
        habit_tracker.save_to_file("habit_data.json")
    else:
        print("Habit not found.")


def delete_habit_menu(habit_tracker):
    """
    Deletes a habit from the habit tracker.

    Args:
        habit_tracker (HabitTracker): The habit tracker instance.

    """
    habit_name = input("Enter the habit name: ")
    habit = find_habit_by_name(habit_tracker, habit_name)
    if habit:
        habit_tracker.delete_habit(habit)
        print("Habit deleted successfully.")
    else:
        print("Habit not found.")
    habit_tracker.save_to_file("habit_data.json")


def list_all_habits(habit_tracker):
    """
    Lists all tracked habits in the habit tracker.

    Args:
        habit_tracker (HabitTracker): The habit tracker instance.

    """
    habits = habit_tracker.get_all_habits()
    print("All Tracked Habits:", len(habits))
    for habit in habits:
        print(f"- {habit.name} ({habit.periodicity})")


def list_habits_by_periodicity(habit_tracker):
    """
    Lists habits based on the specified periodicity.

    Args:
        habit_tracker (HabitTracker): The habit tracker instance.

    """
    periodicity = input("Enter the habit periodicity (daily/weekly): ")
    habits = habit_tracker.get_habits_by_periodicity(periodicity)
    print(f"All {periodicity.capitalize()} Habits:", len(habits))
    for habit in habits:
        print(f"- {habit.name}")


def get_longest_streak_for_habit(habit_tracker):
    """
    Retrieves the longest streak for a specific habit.

    Args:
        habit_tracker (HabitTracker): The habit tracker instance.

    """
    habit_name = input("Enter the habit name: ")
    habit = find_habit_by_name(habit_tracker, habit_name)
    if habit:
        streak = habit_tracker.get_longest_streak_for_habit(habit.name)
        print(f"Longest streak for habit '{habit.name}': {streak}")
    else:
        print("Habit not found.")


def get_longest_streak_for_all_habits(habit_tracker):
    """
    Retrieves the longest streak among all habits.

    Args:
        habit_tracker (HabitTracker): The habit tracker instance.

    """
    streak = habit_tracker.get_longest_streak_for_all_habits()
    print(f"Longest streak for all habits: {streak}")


def find_habit_by_name(habit_tracker, name):
    """
    Finds a habit in the habit tracker by its name.

    Args:
        habit_tracker (HabitTracker): The habit tracker instance.
        name (str): The name of the habit to find.

    Returns:
        Habit or None: The found habit or None if not found.

    """
    habits = habit_tracker.get_all_habits()
    for habit in habits:
        if habit.name.lower() == name.lower():
            return habit
    return None


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
