from enum import Enum


class CreateServiceDowntimeDowntimeType(str, Enum):
    SERVICE = "service"
    SERVICEGROUP = "servicegroup"
    SERVICE_BY_QUERY = "service_by_query"

    def __str__(self) -> str:
        return str(self.value)
