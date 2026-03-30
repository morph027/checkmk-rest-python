from enum import Enum


class UpdateAndAcknowledgeWithQueryPhase(str, Enum):
    ACK = "ack"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
