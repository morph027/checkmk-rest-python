from enum import Enum


class AuthenticationMethod(str, Enum):
    PLAINTEXT = "plaintext"

    def __str__(self) -> str:
        return str(self.value)
