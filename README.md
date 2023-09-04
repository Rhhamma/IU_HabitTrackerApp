# IU_HabitTrackerApp
Habit Tracker is a simple Python command-line application that helps you track your habits and monitor your streaks. It allows you to create habits, mark them as completed, and provides information on the longest streak for individual habits as well as across all habits.

## Table of Contents
- Modules
- [Usage](#usage)
- [Features](#features)
- Unit Tests

  
## Modules
habit_tracker.py:  This module defines two classes: Habit and HabitTracker.
The Habit class represents a habit with name, periodicity (daily or weekly), creation date, and completed dates.
The HabitTracker class manages the list of habits, allowing you to add, delete and list the habits.

analytics.py : contains the functions that provide the user interface for interacting with the Habit Tracker.
Functions like create_habit, complete_task, delete_habit_menu, and others allow you to perform the actions you need from this App .

habit_test.py : defines test cases for the Habit and HabitTracker classes.
It ensures the functionality of habit creation, completion, deletion, and streak calculation is working as expected.

cli.py : this module is the one that the user interract with.
It initializes a HabitTracker instance, loads existing data from a JSON file, and provides a command-line menu for interacting with the Habit Tracker.
Users can create habits, mark tasks as completed, delete habits, list all habits, list habits by periodicity, and get streak information.

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
