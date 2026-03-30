from enum import Enum


class FilterParamsPhase(str, Enum):
    ACK = "ack"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
