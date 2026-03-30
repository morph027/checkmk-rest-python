from enum import Enum


class UpdateAndAcknowledgeWithQueryFilterType(str, Enum):
    ALL = "all"
    PARAMS = "params"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
