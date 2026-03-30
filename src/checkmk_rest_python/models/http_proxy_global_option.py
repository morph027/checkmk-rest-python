from enum import Enum


class HttpProxyGlobalOption(str, Enum):
    ENVIRONMENT = "environment"
    GLOBAL = "global"
    NO_PROXY = "no_proxy"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
