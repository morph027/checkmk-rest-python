from enum import Enum


class CreateHostQueryCommentCommentType(str, Enum):
    HOST = "host"
    HOST_BY_QUERY = "host_by_query"

    def __str__(self) -> str:
        return str(self.value)
