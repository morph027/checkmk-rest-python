from enum import Enum


class AlwaysBulkWhenToBulk(str, Enum):
    ALWAYS = "always"
    TIMEPERIOD = "timeperiod"

    def __str__(self) -> str:
        return str(self.value)
