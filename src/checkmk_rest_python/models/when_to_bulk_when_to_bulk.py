from enum import Enum


class WhenToBulkWhenToBulk(str, Enum):
    ALWAYS = "always"
    TIMEPERIOD = "timeperiod"

    def __str__(self) -> str:
        return str(self.value)
