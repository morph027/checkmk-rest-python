from enum import Enum


class CheckboxWithMgmtTypePriorityValueValue(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    LOW = "low"
    MODERATE = "moderate"

    def __str__(self) -> str:
        return str(self.value)
