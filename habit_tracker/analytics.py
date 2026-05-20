"""
analytics.py

Analytics module implemented in a functional style:
methods compute results from input habits without mutating them.
"""

from typing import List, Dict
from .habit import Habit


class Analytics:
    """
    Pure analytics functions for habit data (functional style).

    No side effects:
    - does not print
    - does not write to disk
    - does not modify habit objects
    """

    @staticmethod
    def list_habits(habits: List[Habit]) -> List[str]:
        """Return the names of all habits."""
        return [h.name for h in habits]

    @staticmethod
    def filter_by_periodicity(habits: List[Habit], periodicity: str) -> List[Habit]:
        """Return all habits matching a given periodicity ('daily' or 'weekly')."""
        return [h for h in habits if h.periodicity == periodicity]

    @staticmethod
    def longest_streak_all(habits: List[Habit]) -> int:
        """Return the longest streak among all habits."""
        if not habits:
            return 0
        return max(h.longest_streak() for h in habits)

    @staticmethod
    def longest_streak_per_habit(habits: List[Habit]) -> Dict[str, int]:
        """Return a mapping of habit name -> longest streak."""
        return {h.name: h.longest_streak() for h in habits}