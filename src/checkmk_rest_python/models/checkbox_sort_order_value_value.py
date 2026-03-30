from enum import Enum


class CheckboxSortOrderValueValue(str, Enum):
    NEWEST_FIRST = "newest_first"
    OLDEST_FIRST = "oldest_first"

    def __str__(self) -> str:
        return str(self.value)
