from enum import Enum


class AcknowledgeServiceQueryProblemAcknowledgeType(str, Enum):
    SERVICE_BY_QUERY = "service_by_query"

    def __str__(self) -> str:
        return str(self.value)
