"""
main.py

Entry point for the Habit Tracker application.

This script puts together the main components:
- JSONStorage: persistence layer (JSON file)
- HabitTracker: core application logic (manages habits)
- HabitCLI: command-line interface for user interaction

Run:
    python main.py
"""

from habit_tracker.storage import JSONStorage
from habit_tracker.tracker import HabitTracker
from habit_tracker.cli import HabitCLI


def main() -> None:
    """
    Start the Habit Tracker application.

    Creates storage, loads/initializes habits through HabitTracker,
    and launches the interactive CLI menu.
    """
    storage = JSONStorage("data/habits.json")
    tracker = HabitTracker(storage)
    cli = HabitCLI(tracker)
    cli.run()


if __name__ == "__main__":
    main()