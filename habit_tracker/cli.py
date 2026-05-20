"""
cli.py

Command Line Interface (CLI) for the Habit Tracker application.

This module provides a simple interactive menu that allows users to:
- Create habits (daily/weekly)
- Complete habits
- Delete habits
- View analytics (list/filter habits, longest streaks)

The CLI layer is responsible only for:
- reading user input
- printing outputs/messages
- calling the underlying HabitTracker and Analytics logic

All business logic remains in the HabitTracker / Habit / Analytics modules.
"""

from __future__ import annotations

from .tracker import HabitTracker
from .analytics import Analytics
from .exceptions import HabitError, InvalidPeriodicityError


class HabitCLI:
    """
    Interactive text-based user interface for the Habit Tracker.

    The CLI displays a menu, handles user input, and calls the appropriate
    HabitTracker methods and Analytics functions.

    Design notes:
    - The CLI catches and displays user-friendly error messages.
    - Business logic errors are raised as exceptions in the core logic
      and handled here to keep the application architecture clean.
    """

    def __init__(self, tracker: HabitTracker) -> None:
        """
        Initialize the CLI with a HabitTracker instance.

        Args:
            tracker: The HabitTracker managing all habit operations and persistence.
        """
        self.tracker = tracker

    def run(self) -> None:
        """
        Run the interactive menu loop until the user exits.

        This method continuously displays the menu, reads a choice,
        and dispatches to the correct handler.
        """
        while True:
            self._print_menu()
            choice = input("Enter choice: ").strip()

            try:
                if choice == "1":
                    self._handle_add_habit()
                elif choice == "2":
                    self._handle_complete_habit()
                elif choice == "3":
                    self._handle_delete_habit()
                elif choice == "4":
                    self._handle_show_all_habits()
                elif choice == "5":
                    self._handle_filter_by_periodicity()
                elif choice == "6":
                    self._handle_longest_streak_overall()
                elif choice == "7":
                    self._handle_longest_streak_per_habit()
                elif choice == "8":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a number from 1 to 8.")

            except (HabitError, InvalidPeriodicityError) as e:
                # Expected business-rule errors (e.g. habit not found, duplicate habit)
                print(f"Error: {e}")
            except Exception as e:
                # Unexpected errors: still show something helpful without crashing silently
                print(f"Unexpected error: {e}")

    def _print_menu(self) -> None:
        """
        Print the main menu options.
        """
        print("\nHabit Tracker Menu:")
        print("1. Add habit")
        print("2. Complete habit")
        print("3. Delete habit")
        print("4. Show all habits")
        print("5. Filter by periodicity")
        print("6. Longest streak overall")
        print("7. Longest streak per habit")
        print("8. Exit")

    def _handle_add_habit(self) -> None:
        """
        Create a new habit using user input.

        Prompts for:
        - habit name
        - periodicity ('daily' or 'weekly')
        """
        name = input("Habit name: ").strip()
        periodicity = input("Periodicity (daily/weekly): ").strip().lower()

        if periodicity not in ("daily", "weekly"):
            raise InvalidPeriodicityError("Periodicity must be 'daily' or 'weekly'.")

        self.tracker.add_habit(name, periodicity)  # type: ignore[arg-type]
        print("Habit added.")

    def _handle_complete_habit(self) -> None:
        """
        Record a completion for an existing habit.

        Prompts for:
        - habit name
        """
        name = input("Habit name: ").strip()
        self.tracker.complete_habit(name)
        print("Completion added.")

    def _handle_delete_habit(self) -> None:
        """
        Delete an existing habit.

        Prompts for:
        - habit name
        """
        name = input("Habit name: ").strip()
        self.tracker.delete_habit(name)
        print("Habit deleted.")

    def _handle_show_all_habits(self) -> None:
        """
        Display the names of all current habits.
        """
        names = Analytics.list_habits(self.tracker.habits)
        print("All habits:", names)

    def _handle_filter_by_periodicity(self) -> None:
        """
        Display habits filtered by periodicity ('daily' or 'weekly').

        Prompts for:
        - periodicity
        """
        periodicity = input("Periodicity (daily/weekly): ").strip().lower()
        if periodicity not in ("daily", "weekly"):
            raise InvalidPeriodicityError("Periodicity must be 'daily' or 'weekly'.")

        filtered = Analytics.filter_by_periodicity(self.tracker.habits, periodicity)
        print(f"{periodicity.capitalize()} habits:", [h.name for h in filtered])

    def _handle_longest_streak_overall(self) -> None:
        """
        Display the longest streak across all habits.
        """
        value = Analytics.longest_streak_all(self.tracker.habits)
        print("Longest streak overall:", value)

    def _handle_longest_streak_per_habit(self) -> None:
        """
        Display the longest streak for each habit.
        """
        result = Analytics.longest_streak_per_habit(self.tracker.habits)
        print("Longest streak per habit:", result)