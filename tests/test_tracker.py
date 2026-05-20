from habit_tracker.storage import JSONStorage
from habit_tracker.tracker import HabitTracker
from habit_tracker.exceptions import DuplicateHabitError, HabitNotFoundError


def test_tracker_add_and_delete(tmp_path):
    storage = JSONStorage(str(tmp_path / "habits.json"))
    tracker = HabitTracker(storage)

    # fixtures will auto-generate; we can still add more than 5
    tracker.add_habit("New Habit", "daily")
    assert tracker.get_habit("New Habit").name == "New Habit"

    tracker.delete_habit("New Habit")
    try:
        tracker.get_habit("New Habit")
        assert False, "Expected HabitNotFoundError"
    except HabitNotFoundError:
        assert True


def test_duplicate_habit_rejected(tmp_path):
    storage = JSONStorage(str(tmp_path / "habits.json"))
    tracker = HabitTracker(storage)

    tracker.add_habit("Duplicate", "daily")
    try:
        tracker.add_habit("Duplicate", "daily")
        assert False, "Expected DuplicateHabitError"
    except DuplicateHabitError:
        assert True