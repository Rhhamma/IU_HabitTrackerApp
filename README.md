# IU_HabitTrackerApp
Habit Tracker is a simple Python command-line application that helps you track your habits and monitor your streaks. It allows you to create habits, mark them as completed, and provides information on the longest streak for individual habits as well as across all habits.

## Table of Contents
- [Usage](#usage)
- [Features](#features)
- Unit Tests

## Usage
After installing the dependencies, download the files from this repository (if not downloaded already) and store them in a separate folder. Open your command/terminal window and cd to your downloaded folder

To start the Habit Tracker application, run the following command:
    $ python cli.py
    The application will present a menu with various options:

       - Create a habit: Create a new habit and specify its name, periodicity, and creation date.
       - Complete a task: Mark a habit as completed by specifying the habit name and completion date.
       - Delete a habit: Remove a habit from the tracker by providing its name.
       - List all habits: Display a list of all tracked habits.
       - List habits by periodicity: Show habits based on their periodicity (daily or weekly).
       - Get longest streak for a habit: Retrieve the longest streak for a specific habit.
       - Get longest streak for all habits: Calculate and display the longest streak across all habits.
       - Exit: Quit the application.
       - Follow the prompts and provide the required information for each option.

## Features
    -Create habits with a specified name, periodicity, and creation date.
    -Mark habits as completed by specifying the habit name and completion date.
    -Delete habits from the tracker.
    -View a list of all tracked habits.
    -List habits based on their periodicity (daily or weekly).
    -Retrieve the longest streak for a specific habit.
    -Calculate and display the longest streak across all habits.


## Unit Tests
The habit_test.py file contains unit tests to assure the program functionality. You can run the tests using the following command:

python -m unittest habit_test.py



Enjoy tracking your habits with the Habit Tracker program!
