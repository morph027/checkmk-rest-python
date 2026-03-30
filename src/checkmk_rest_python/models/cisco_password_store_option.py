from enum import Enum


class CiscoPasswordStoreOption(str, Enum):
    EXPLICIT = "explicit"
    STORE = "store"

    def __str__(self) -> str:
        return str(self.value)
