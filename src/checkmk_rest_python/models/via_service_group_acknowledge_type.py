from enum import Enum


class ViaServiceGroupAcknowledgeType(str, Enum):
    SERVICEGROUP = "servicegroup"

    def __str__(self) -> str:
        return str(self.value)
