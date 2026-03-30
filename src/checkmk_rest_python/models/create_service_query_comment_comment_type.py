from enum import Enum


class CreateServiceQueryCommentCommentType(str, Enum):
    SERVICE = "service"
    SERVICE_BY_QUERY = "service_by_query"

    def __str__(self) -> str:
        return str(self.value)
