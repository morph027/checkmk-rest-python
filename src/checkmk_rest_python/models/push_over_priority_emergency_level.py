from enum import Enum


class PushOverPriorityEmergencyLevel(str, Enum):
    EMERGENCY = "emergency"

    def __str__(self) -> str:
        return str(self.value)
