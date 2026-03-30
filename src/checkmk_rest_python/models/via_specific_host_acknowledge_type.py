from enum import Enum


class ViaSpecificHostAcknowledgeType(str, Enum):
    HOST = "host"

    def __str__(self) -> str:
        return str(self.value)
