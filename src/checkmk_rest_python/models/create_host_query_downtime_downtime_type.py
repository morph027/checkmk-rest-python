from enum import Enum


class CreateHostQueryDowntimeDowntimeType(str, Enum):
    HOST = "host"
    HOSTGROUP = "hostgroup"
    HOST_BY_QUERY = "host_by_query"

    def __str__(self) -> str:
        return str(self.value)
