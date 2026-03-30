from enum import Enum


class AcknowledgeSpecificServiceProblemAcknowledgeType(str, Enum):
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
