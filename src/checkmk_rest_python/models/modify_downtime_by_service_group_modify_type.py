from enum import Enum


class ModifyDowntimeByServiceGroupModifyType(str, Enum):
    BY_ID = "by_id"
    HOSTGROUP = "hostgroup"
    PARAMS = "params"
    QUERY = "query"
    SERVICEGROUP = "servicegroup"

    def __str__(self) -> str:
        return str(self.value)
