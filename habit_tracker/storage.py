"""
storage.py

Persistence layer for the habit tracker.
Stores and loads habits in JSON format.
"""

import json
from pathlib import Path
from typing import List, Dict


class JSONStorage:
    """
    File-based JSON storage for habit data.

    The storage reads and writes a list of habit dictionaries to a JSON file.
    """

    def __init__(self, file_path: str = "data/habits.json") -> None:
        """
        Args:
            file_path: Path to the JSON file used for persistence.
        """
        self.path = Path(file_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, habits: List[Dict]) -> None:
        """
        Save habits to disk.

        Args:
            habits: List of JSON-serializable dictionaries.
        """
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(habits, f, indent=4)

    def load(self) -> List[Dict]:
        """
        Load habits from disk.

        Returns:
            A list of habit dictionaries, or an empty list if file does not exist.
        """
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)