from enum import Enum


class SMSAPIExplicitPasswordOption(str, Enum):
    EXPLICIT = "explicit"
    STORE = "store"

    def __str__(self) -> str:
        return str(self.value)
