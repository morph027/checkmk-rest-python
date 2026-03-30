from enum import Enum


class LDAPUsersUserIdCase(str, Enum):
    CONVERT_TO_LOWERCASE = "convert_to_lowercase"
    DONT_CONVERT_TO_LOWERCASE = "dont_convert_to_lowercase"

    def __str__(self) -> str:
        return str(self.value)
