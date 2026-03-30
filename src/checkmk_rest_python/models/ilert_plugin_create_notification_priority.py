from enum import Enum


class IlertPluginCreateNotificationPriority(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"

    def __str__(self) -> str:
        return str(self.value)
