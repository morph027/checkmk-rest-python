from enum import Enum


class UpdateAndAcknowledgeWithParamsFilterType(str, Enum):
    ALL = "all"
    PARAMS = "params"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
