from enum import Enum


class ManagementTypeCaseStatesStartPredefined(str, Enum):
    AWAITING_INFO = "awaiting_info"
    CLOSED = "closed"
    NEW = "new"
    NONE = "none"
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
