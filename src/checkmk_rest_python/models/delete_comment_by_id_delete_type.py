from enum import Enum


class DeleteCommentByIdDeleteType(str, Enum):
    BY_ID = "by_id"
    PARAMS = "params"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
