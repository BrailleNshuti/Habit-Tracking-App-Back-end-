from datetime import datetime, timedelta
from habit_tracker.habit import Habit


def test_habit_creation():
    h = Habit("Exercise", "daily")
    assert h.name == "Exercise"
    assert h.periodicity == "daily"
    assert h.longest_streak() == 0


def test_daily_streak_consecutive_days():
    h = Habit("Exercise", "daily")
    base = datetime(2026, 1, 1, 12, 0, 0)
    h.add_completion(base)
    h.add_completion(base + timedelta(days=1))
    h.add_completion(base + timedelta(days=2))
    assert h.longest_streak() == 3


def test_daily_streak_break_on_gap():
    h = Habit("Exercise", "daily")
    base = datetime(2026, 1, 1, 12, 0, 0)
    h.add_completion(base)
    h.add_completion(base + timedelta(days=2))  # gap day 1 missing
    assert h.longest_streak() == 1


def test_weekly_streak_consecutive_weeks():
    h = Habit("Call Family", "weekly")
    base = datetime(2026, 1, 5, 12, 0, 0)  # a Monday
    h.add_completion(base)
    h.add_completion(base + timedelta(days=7))
    h.add_completion(base + timedelta(days=14))
    h.add_completion(base + timedelta(days=21))
    assert h.longest_streak() == 4