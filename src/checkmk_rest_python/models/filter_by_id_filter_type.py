from enum import Enum


class FilterByIdFilterType(str, Enum):
    BY_ID = "by_id"
    PARAMS = "params"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
