from enum import Enum


class AcknowledgeHostGroupProblemAcknowledgeType(str, Enum):
    HOSTGROUP = "hostgroup"

    def __str__(self) -> str:
        return str(self.value)
