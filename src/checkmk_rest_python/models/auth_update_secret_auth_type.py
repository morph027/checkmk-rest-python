from enum import Enum


class AuthUpdateSecretAuthType(str, Enum):
    AUTOMATION = "automation"
    PASSWORD = "password"
    REMOVE = "remove"

    def __str__(self) -> str:
        return str(self.value)
