from enum import Enum


class AuthSecretAuthType(str, Enum):
    AUTOMATION = "automation"
    PASSWORD = "password"

    def __str__(self) -> str:
        return str(self.value)
