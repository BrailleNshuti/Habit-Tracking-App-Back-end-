"""
habit.py

Defines the Habit domain model. A Habit tracks completions and computes streaks
for daily and weekly periodicities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Optional, Literal, Set, Tuple

from .exceptions import InvalidPeriodicityError

Periodicity = Literal["daily", "weekly"]


def _iso_week(d: date) -> Tuple[int, int]:
    """
    Convert a date into an ISO week identifier.

    Returns:
        (iso_year, iso_week)
    """
    iso_year, iso_week, _ = d.isocalendar()
    return iso_year, iso_week


def _is_consecutive_iso_week(prev: Tuple[int, int], curr: Tuple[int, int]) -> bool:
    """
    Check whether two ISO week identifiers are consecutive.

    Handles year boundaries (e.g. 2025-W52 -> 2026-W01).
    """
    prev_year, prev_week = prev
    curr_year, curr_week = curr

    # Same year, next week
    if curr_year == prev_year and curr_week == prev_week + 1:
        return True

    # Year rollover: previous year ends on week 52 or 53, next year starts at week 1
    if curr_year == prev_year + 1 and curr_week == 1 and prev_week in (52, 53):
        return True

    return False


@dataclass
class Habit:
    """
    Represents a single habit.

    Attributes:
        name: Unique name of the habit.
        periodicity: "daily" or "weekly".
        created_at: Timestamp when habit was created.
        completions: List of completion timestamps.

    Behavior:
        - add_completion(): record completion timestamp
        - longest_streak(): compute longest streak of consecutive periods
    """

    name: str
    periodicity: Periodicity
    created_at: datetime = field(default_factory=datetime.now)
    completions: List[datetime] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate and normalize values after dataclass initialization."""
        self.name = self.name.strip()
        if not self.name:
            raise ValueError("Habit name must not be empty.")

        if self.periodicity not in ("daily", "weekly"):
            raise InvalidPeriodicityError("Periodicity must be 'daily' or 'weekly'.")

    def add_completion(self, when: Optional[datetime] = None) -> None:
        """
        Record a completion.

        Args:
            when: Optional completion datetime. If None, current time is used.
        """
        when = when or datetime.now()
        self.completions.append(when)
        self.completions.sort()

    def completed_periods(self) -> List[object]:
        """
        Get unique completed periods for this habit.

        Returns:
            For daily habits: list[date]
            For weekly habits: list[tuple[int, int]] representing (iso_year, iso_week)
        """
        if not self.completions:
            return []

        if self.periodicity == "daily":
            periods: Set[date] = {c.date() for c in self.completions}
            return sorted(periods)

        periods_w: Set[Tuple[int, int]] = {_iso_week(c.date()) for c in self.completions}
        return sorted(periods_w)

    def longest_streak(self) -> int:
        """
        Compute the longest streak of consecutive completed periods.

        Rules:
            - daily: consecutive calendar days
            - weekly: consecutive ISO weeks (calendar-week based)
        """
        periods = self.completed_periods()
        if not periods:
            return 0

        if self.periodicity == "daily":
            # periods is list[date]
            max_streak = streak = 1
            for i in range(1, len(periods)):
                if (periods[i] - periods[i - 1]).days == 1:
                    streak += 1
                else:
                    streak = 1
                max_streak = max(max_streak, streak)
            return max_streak

        # weekly: periods is list[(iso_year, iso_week)]
        periods_w = periods  # type: ignore[assignment]
        max_streak = streak = 1
        for i in range(1, len(periods_w)):
            if _is_consecutive_iso_week(periods_w[i - 1], periods_w[i]):
                streak += 1
            else:
                streak = 1
            max_streak = max(max_streak, streak)
        return max_streak

    def to_dict(self) -> dict:
        """
        Serialize the Habit into a JSON-safe dictionary.
        """
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [c.isoformat() for c in self.completions],
        }

    @staticmethod
    def from_dict(data: dict) -> "Habit":
        """
        Deserialize a Habit from a dictionary loaded from JSON.
        """
        habit = Habit(name=data["name"], periodicity=data["periodicity"])
        habit.created_at = datetime.fromisoformat(data["created_at"])
        habit.completions = [datetime.fromisoformat(c) for c in data.get("completions", [])]
        habit.completions.sort()
        return habit