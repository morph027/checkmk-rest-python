from enum import Enum


class TimePeriodWhenToBulk(str, Enum):
    ALWAYS = "always"
    TIMEPERIOD = "timeperiod"

    def __str__(self) -> str:
        return str(self.value)
