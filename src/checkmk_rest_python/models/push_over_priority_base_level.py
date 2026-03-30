from enum import Enum


class PushOverPriorityBaseLevel(str, Enum):
    HIGH = "high"
    LOW = "low"
    LOWEST = "lowest"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
