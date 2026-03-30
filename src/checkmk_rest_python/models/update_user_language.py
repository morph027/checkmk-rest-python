from enum import Enum


class UpdateUserLanguage(str, Enum):
    DE = "de"
    EN = "en"
    RO = "ro"

    def __str__(self) -> str:
        return str(self.value)
