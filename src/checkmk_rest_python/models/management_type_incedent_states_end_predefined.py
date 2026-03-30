from enum import Enum


class ManagementTypeIncedentStatesEndPredefined(str, Enum):
    CANCELED = "canceled"
    CLOSED = "closed"
    HOLD = "hold"
    NEW = "new"
    NONE = "none"
    PROGRESS = "progress"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
