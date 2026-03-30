from enum import Enum


class ViaSpecificServiceAcknowledgeType(str, Enum):
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
