from enum import Enum


class UseLiveStatusDaemonUseLivestatusDaemon(str, Enum):
    DIRECT = "direct"
    WITH_PROXY = "with_proxy"

    def __str__(self) -> str:
        return str(self.value)
