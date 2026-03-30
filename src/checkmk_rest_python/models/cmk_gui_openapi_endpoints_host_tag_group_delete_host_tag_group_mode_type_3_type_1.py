from enum import Enum


class CmkGuiOpenapiEndpointsHostTagGroupDeleteHostTagGroupModeType3Type1(str, Enum):
    ABORT = "abort"
    DELETE = "delete"
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
