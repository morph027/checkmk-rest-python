from enum import Enum


class UpdateAndAcknowledgeFilterPhase(str, Enum):
    ACK = "ack"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
