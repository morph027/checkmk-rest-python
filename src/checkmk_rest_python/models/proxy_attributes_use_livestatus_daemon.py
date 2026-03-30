from enum import Enum


class ProxyAttributesUseLivestatusDaemon(str, Enum):
    DIRECT = "direct"
    WITH_PROXY = "with_proxy"

    def __str__(self) -> str:
        return str(self.value)
