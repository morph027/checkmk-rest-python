from enum import Enum


class AuthPasswordAuthType(str, Enum):
    AUTOMATION = "automation"
    PASSWORD = "password"

    def __str__(self) -> str:
        return str(self.value)
