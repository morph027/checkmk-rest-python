from enum import Enum


class CmkGuiOpenapiEndpointsDowntimeShowDowntimesDowntimeType(str, Enum):
    BOTH = "both"
    HOST = "host"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
