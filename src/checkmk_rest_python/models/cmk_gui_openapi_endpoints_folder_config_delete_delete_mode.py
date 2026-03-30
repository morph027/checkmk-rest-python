from enum import Enum


class CmkGuiOpenapiEndpointsFolderConfigDeleteDeleteMode(str, Enum):
    ABORT_ON_NONEMPTY = "abort_on_nonempty"
    RECURSIVE = "recursive"

    def __str__(self) -> str:
        return str(self.value)
