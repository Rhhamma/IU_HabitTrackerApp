import unittest
from datetime import date
from habit_tracker import Habit, HabitTracker

class HabitTest(unittest.TestCase):

    def setUp(self):
        # Create a habit tracker
        self.habit_tracker = HabitTracker()

    def test_create_habit(self):
        # Create a habit
        habit = Habit("Exercise", "daily", date(2023, 7, 1))

        # Add the habit to the habit tracker
        self.habit_tracker.add_habit(habit)

        # Check if the habit is added successfully
        self.assertIn(habit, self.habit_tracker.get_all_habits())

    def test_complete_task(self):
        # Create a habit
        habit = Habit("Exercise", "daily", date(2023, 7, 1))

        # Add the habit to the habit tracker
        self.habit_tracker.add_habit(habit)

        # Complete a task for the habit
        habit.complete_task(date(2023, 7, 2))

        # Check if the task is marked as completed
        self.assertTrue(habit.is_completed(date(2023, 7, 2)))

    def test_delete_habit(self):
        # Create a habit
        habit = Habit("Exercise", "daily", date(2023, 7, 1))

        # Add the habit to the habit tracker
        self.habit_tracker.add_habit(habit)

        # Delete the habit from the habit tracker
        self.habit_tracker.delete_habit(habit)

        # Check if the habit is removed successfully
        self.assertNotIn(habit, self.habit_tracker.get_all_habits())

    def test_list_all_habits(self):
        # Create some habits
        habit1 = Habit("Exercise", "daily", date(2023, 7, 1))
        habit2 = Habit("Read", "daily", date(2023, 7, 1))

        # Add the habits to the habit tracker
        self.habit_tracker.add_habit(habit1)
        self.habit_tracker.add_habit(habit2)

        # Get all habits
        all_habits = self.habit_tracker.get_all_habits()

        # Check if all habits are retrieved
        self.assertCountEqual(all_habits, [habit1, habit2])

    def test_list_habits_by_periodicity(self):
        # Create some habits
        habit1 = Habit("Exercise", "daily", date(2023, 7, 1))
        habit2 = Habit("Clean Room", "weekly", date(2023, 7, 1))

        # Add the habits to the habit tracker
        self.habit_tracker.add_habit(habit1)
        self.habit_tracker.add_habit(habit2)

        # Get habits by periodicity
        daily_habits = self.habit_tracker.get_habits_by_periodicity("daily")
        weekly_habits = self.habit_tracker.get_habits_by_periodicity("weekly")

        # Check if habits are filtered correctly
        self.assertCountEqual(daily_habits, [habit1])
        self.assertCountEqual(weekly_habits, [habit2])

    def test_get_longest_streak_for_habit(self):
        # Create a habit
        habit = Habit("Exercise", "daily", date(2023, 7, 1))

        # Add the habit to the habit tracker
        self.habit_tracker.add_habit(habit)

        # Complete tasks for the habit
        habit.complete_task(date(2023, 7, 2))
        habit.complete_task(date(2023, 7, 3))
        habit.complete_task(date(2023, 7, 4))

        # Check the longest streak for the habit
        longest_streak = self.habit_tracker.get_longest_streak_for_habit("Exercise")

        # Check if the longest streak is calculated correctly
        self.assertEqual(longest_streak, 3)

    def test_get_longest_streak_for_all_habits(self):
        # Create some habits
        habit1 = Habit("Exercise", "daily", date(2023, 7, 1))
        habit2 = Habit("Read", "daily", date(2023, 7, 1))
        habit3 = Habit("Clean Room", "weekly", date(2023, 7, 1))

        # Add the habits to the habit tracker
        self.habit_tracker.add_habit(habit1)
        self.habit_tracker.add_habit(habit2)
        self.habit_tracker.add_habit(habit3)

        # Complete tasks for the habits
        habit1.complete_task(date(2023, 7, 2))
        habit1.complete_task(date(2023, 7, 3))
        habit1.complete_task(date(2023, 7, 4))

        habit2.complete_task(date(2023, 7, 2))
        habit2.complete_task(date(2023, 7, 4))

        habit3.complete_task(date(2023, 7, 2))
        habit3.complete_task(date(2023, 7, 3))

        # Check the longest streak for all habits
        longest_streak_all_habits = self.habit_tracker.get_longest_streak_for_all_habits()

        # Check if the longest streak for all habits is calculated correctly
        self.assertEqual(longest_streak_all_habits, 3)

if __name__ == '__main__':
    unittest.main()
