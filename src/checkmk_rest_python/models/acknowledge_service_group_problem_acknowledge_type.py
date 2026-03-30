from enum import Enum


class AcknowledgeServiceGroupProblemAcknowledgeType(str, Enum):
    SERVICEGROUP = "servicegroup"

    def __str__(self) -> str:
        return str(self.value)
