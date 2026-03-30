from enum import Enum


class ViaHostGroupAcknowledgeType(str, Enum):
    HOSTGROUP = "hostgroup"

    def __str__(self) -> str:
        return str(self.value)
