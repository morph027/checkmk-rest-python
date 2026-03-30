from enum import Enum


class FilterParamsUpdateAndAcknowledgeState(str, Enum):
    CRITICAL = "critical"
    OK = "ok"
    UNKNOWN = "unknown"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
