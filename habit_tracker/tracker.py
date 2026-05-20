from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from .exceptions import DuplicateHabitError, HabitNotFoundError
from .fixtures import generate_fixtures
from .habit import Habit, Periodicity
from .storage import JSONStorage


class HabitTracker:
    """
    Manages multiple Habit objects.

    Responsibilities:
    - create and delete habits
    - record habit completions
    - load and save habits using JSONStorage
    - auto-generate predefined habits + 4 weeks of data if storage is empty
    """

    def __init__(self, storage: JSONStorage) -> None:
        self.storage = storage
        self.habits: List[Habit] = []
        self.load()

    def add_habit(self, name: str, periodicity: Periodicity) -> Habit:
        name_clean = name.strip()
        if any(h.name == name_clean for h in self.habits):
            raise DuplicateHabitError(f"Habit '{name_clean}' already exists.")

        habit = Habit(name=name_clean, periodicity=periodicity)
        self.habits.append(habit)
        self.save()
        return habit

    def delete_habit(self, name: str) -> None:
        name_clean = name.strip()
        before = len(self.habits)

        self.habits = [h for h in self.habits if h.name != name_clean]

        if len(self.habits) == before:
            raise HabitNotFoundError(f"Habit '{name_clean}' not found.")

        self.save()

    def complete_habit(self, name: str, when: Optional[datetime] = None) -> None:
        habit = self.get_habit(name)
        habit.add_completion(when)
        self.save()

    def get_habit(self, name: str) -> Habit:
        name_clean = name.strip()
        for h in self.habits:
            if h.name == name_clean:
                return h
        raise HabitNotFoundError(f"Habit '{name_clean}' not found.")

    def save(self) -> None:
        """Persist habits to JSON storage."""
        self.storage.save([h.to_dict() for h in self.habits])

    def load(self) -> None:
        """
        Load habits from JSON storage.
        If storage is empty or missing, generate fixtures (5 habits + 4 weeks data).
        """
        data: list[dict] = self.storage.load()

        if not data:
            self.habits = generate_fixtures()
            self.save()
            return

        self.habits = [Habit.from_dict(d) for d in data]