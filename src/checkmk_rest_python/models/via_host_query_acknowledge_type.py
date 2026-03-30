from enum import Enum


class ViaHostQueryAcknowledgeType(str, Enum):
    HOST_BY_QUERY = "host_by_query"

    def __str__(self) -> str:
        return str(self.value)
