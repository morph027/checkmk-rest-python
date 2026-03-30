from enum import Enum


class SignL4TeamSecretStoreIDOption(str, Enum):
    EXPLICIT = "explicit"
    STORE = "store"

    def __str__(self) -> str:
        return str(self.value)
