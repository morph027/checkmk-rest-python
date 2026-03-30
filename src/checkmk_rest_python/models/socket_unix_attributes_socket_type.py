from enum import Enum


class SocketUnixAttributesSocketType(str, Enum):
    LOCAL = "local"
    TCP = "tcp"
    TCP6 = "tcp6"
    UNIX = "unix"

    def __str__(self) -> str:
        return str(self.value)
