from enum import Enum


class CheckboxOpsGeniePriorityValueValue(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    INFORMATIONAL = "informational"
    LOW = "low"
    MODERATE = "moderate"

    def __str__(self) -> str:
        return str(self.value)
