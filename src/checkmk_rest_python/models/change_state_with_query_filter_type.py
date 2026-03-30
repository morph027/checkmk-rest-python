from enum import Enum


class ChangeStateWithQueryFilterType(str, Enum):
    PARAMS = "params"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
