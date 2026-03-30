from enum import Enum


class ChangeStateWithParamsFilterType(str, Enum):
    PARAMS = "params"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
