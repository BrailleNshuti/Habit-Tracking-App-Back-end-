"""
exceptions.py

Custom exception classes for clearer error handling in the habit tracker.
"""


class HabitError(Exception):
    """Base exception for habit tracker errors."""


class DuplicateHabitError(HabitError):
    """Raised when trying to create a habit with an existing name."""


class HabitNotFoundError(HabitError):
    """Raised when a habit cannot be found by name."""


class InvalidPeriodicityError(HabitError):
    """Raised when periodicity is not supported (daily/weekly)."""