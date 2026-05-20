from datetime import datetime, timedelta
from habit_tracker.habit import Habit
from habit_tracker.analytics import Analytics


def test_list_habits():
    habits = [Habit("A", "daily"), Habit("B", "weekly")]
    assert Analytics.list_habits(habits) == ["A", "B"]


def test_filter_by_periodicity():
    habits = [Habit("A", "daily"), Habit("B", "weekly"), Habit("C", "daily")]
    daily = Analytics.filter_by_periodicity(habits, "daily")
    assert [h.name for h in daily] == ["A", "C"]


def test_longest_streak_all():
    h1 = Habit("H1", "daily")
    h2 = Habit("H2", "daily")

    base = datetime(2026, 1, 1, 12, 0, 0)
    h1.add_completion(base)
    h1.add_completion(base + timedelta(days=1))  # streak 2
    h2.add_completion(base)  # streak 1

    assert Analytics.longest_streak_all([h1, h2]) == 2