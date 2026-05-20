"""
fixtures.py

Creates predefined habits and example tracking data (4 weeks).
Used to auto-initialize the application when storage is empty.
"""

from datetime import datetime, timedelta
from typing import List
from .habit import Habit


def generate_fixtures(now: datetime | None = None) -> List[Habit]:
    """
    Generate 5 predefined habits and 4 weeks of example completions.

    Returns:
        List of Habit objects with completion history.
    """
    now = now or datetime.now()
    start = (now - timedelta(days=27)).replace(hour=12, minute=0, second=0, microsecond=0)

    habits = [
        Habit("Exercise", "daily"),
        Habit("Drink Water", "daily"),
        Habit("Read 10 Pages", "daily"),
        Habit("Call Family", "weekly"),
        Habit("Clean Room", "weekly"),
    ]

    # 4 weeks (28 days) of daily completions
    for day in range(28):
        d = start + timedelta(days=day)

        # Exercise: skip one day to demonstrate streak break
        if day != 10:
            habits[0].add_completion(d)

        # Drink Water: perfect 28-day streak
        habits[1].add_completion(d)

        # Read: every second day
        if day % 2 == 0:
            habits[2].add_completion(d)

    # 4 consecutive weeks (weekly habits)
    for week in range(4):
        w = start + timedelta(days=week * 7)
        habits[3].add_completion(w)
        habits[4].add_completion(w)

    return habits