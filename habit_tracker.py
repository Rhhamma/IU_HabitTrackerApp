import os
from datetime import datetime, timedelta
import json


class Habit:
    """
    Represents a habit with its name, periodicity, created date, and completed dates.
    """

    def __init__(self, name, periodicity, created_date, completed_dates=None):
        """
        Initializes a new Habit object.

        Args:
            name (str): The name of the habit.
            periodicity (str): The periodicity of the habit (daily or weekly).
            created_date (datetime.date): The date when the habit was created.
            completed_dates (list, optional): List of completed dates. Defaults to None.
        """
        self.name = name
        self.periodicity = periodicity
        self.created_date = created_date
        self.completed_dates = completed_dates if completed_dates is not None else []

    def __str__(self):
        """
        Returns a string representation of the Habit object.

        Returns:
            str: String representation of the Habit object.
        """
        return f"{self.name} ({self.periodicity})"

    def complete_task(self, date):
        """
        Marks the task as completed for the specified date.

        Args:
            date (datetime.date): The date when the task was completed.
        """
        self.completed_dates.append(date)

    def is_completed(self, date):
        """
        Checks if the habit is completed for the specified date.

        Args:
            date (datetime.date): The date to check.

        Returns:
            bool: True if the habit is completed for the date, False otherwise.
        """
        return date in self.completed_dates

    def get_streak(self):
        """
        Calculates the current streak of completing the habit.

        Returns:
            int: The current streak of completing the habit.
        """
        current_streak = 0
        today = datetime.today().date()

        for i in range(len(self.completed_dates) - 1, -1, -1):
            if self.completed_dates[i] == today - timedelta(days=current_streak):
                current_streak += 1
            else:
                break

        return current_streak

    def get_longest_streak(self):
        """
        Calculates the longest streak of completing the habit.

        Returns:
            int: The longest streak of completing the habit.
        """
        sorted_dates = sorted(self.completed_dates)
        longest_streak = 0
        current_streak = 0
        previous_date = None

        for date in sorted_dates:
            if previous_date is None or date == previous_date + timedelta(days=1):
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 1

            previous_date = date

        if current_streak > longest_streak:
            longest_streak = current_streak

        return longest_streak


class HabitTracker:
    """
    Represents a habit tracker that manages a list of habits.
    """

    def __init__(self):
        """
        Initializes a new HabitTracker object.
        """
        self.habits = []

    def add_habit(self, habit):
        """
        Adds a habit to the habit tracker.

        Args:
            habit (Habit): The habit to add.
        """
        self.habits.append(habit)

    def delete_habit(self, habit):
        """
        Deletes a habit from the habit tracker.

        Args:
            habit (Habit): The habit to delete.
        """
        self.habits.remove(habit)

    def get_all_habits(self):
        """
        Retrieves all habits in the habit tracker.

        Returns:
            list: List of all habits in the habit tracker.
        """
        return self.habits

    def get_habits_by_periodicity(self, periodicity):
        """
        Retrieves habits in the habit tracker based on the specified periodicity.

        Args:
            periodicity (str): The periodicity to filter by (daily or weekly).

        Returns:
            list: List of habits that match the specified periodicity.
        """
        return [habit for habit in self.habits if habit.periodicity == periodicity]

    def get_longest_streak_for_habit(self, habit_name):
        """
        Retrieves the longest streak for a specific habit.

        Args:
            habit_name (str): The name of the habit.

        Returns:
            int: The longest streak for the habit.
        """
        habit = self.find_habit_by_name(habit_name)
        if habit:
            return habit.get_longest_streak()
        else:
            return 0

    def find_habit_by_name(self, name):
        """
        Finds a habit in the habit tracker by its name.

        Args:
            name (str): The name of the habit to find.

        Returns:
            Habit or None: The found habit or None if not found.
        """
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                return habit
        return None

    def get_longest_streak_for_all_habits(self):
        """
        Retrieves the longest streak among all habits in the habit tracker.

        Returns:
            int: The longest streak among all habits.
        """
        longest_streak = 0
        for habit in self.habits:
            streak = habit.get_longest_streak()
            if streak > longest_streak:
                longest_streak = streak
        return longest_streak

    def save_to_file(self, filename):
        """
        Saves the habit tracker data to a JSON file.

        Args:
            filename (str): The name of the file to save to.
        """
        data = {
            "habits": [
                {
                    "name": habit.name,
                    "periodicity": habit.periodicity,
                    "created_date": habit.created_date.isoformat(),
                    "completed_dates": [date.isoformat() for date in habit.completed_dates]
                }
                for habit in self.habits
            ]
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename):
        """
        Loads the habit tracker data from a JSON file.

        Args:
            filename (str): The name of the file to load from.
        """
        with open(filename, "r") as file:
            data = json.load(file)

        self.habits = [
            Habit(
                name=habit_data["name"],
                periodicity=habit_data["periodicity"],
                created_date=datetime.fromisoformat(habit_data["created_date"]).date(),
                completed_dates=[datetime.fromisoformat(date).date() for date in habit_data["completed_dates"]]
            )
            for habit_data in data["habits"]
        ]


# Check if the habit_data.json file exists
if not os.path.exists('habit_data.json'):
    # Create 5 instances of predefined habits
    habit1 = Habit("Brush Teeth", "daily", datetime(2023, 5, 1).date())
    habit2 = Habit("Exercise", "daily", datetime(2023, 5, 1).date())
    habit3 = Habit("Read", "daily", datetime(2023, 5, 1).date())
    habit4 = Habit("Clean Room", "weekly", datetime(2023, 5, 1).date())
    habit5 = Habit("Cook", "weekly", datetime(2023, 5, 1).date())

    # Add predefined habits to the habit tracker
    habit_tracker = HabitTracker()
    habit_tracker.add_habit(habit1)
    habit_tracker.add_habit(habit2)
    habit_tracker.add_habit(habit3)
    habit_tracker.add_habit(habit4)
    habit_tracker.add_habit(habit5)

    # Save example tracking data
    habit_tracker.save_to_file("habit_data.json")
else:
    pass
