from enum import Enum


class CmkGuiOpenapiEndpointsCommentShowCommentsCollectionName(str, Enum):
    ALL = "all"
    HOST = "host"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
