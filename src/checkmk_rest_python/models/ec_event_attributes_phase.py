from enum import Enum


class ECEventAttributesPhase(str, Enum):
    ACK = "ack"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
