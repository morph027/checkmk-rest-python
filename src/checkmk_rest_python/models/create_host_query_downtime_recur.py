from enum import Enum


class CreateHostQueryDowntimeRecur(str, Enum):
    DAY = "day"
    DAY_OF_MONTH = "day_of_month"
    FIXED = "fixed"
    FOURTH_WEEK = "fourth_week"
    HOUR = "hour"
    SECOND_WEEK = "second_week"
    WEEK = "week"
    WEEKDAY_END = "weekday_end"
    WEEKDAY_START = "weekday_start"

    def __str__(self) -> str:
        return str(self.value)
