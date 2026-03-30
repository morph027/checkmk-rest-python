from enum import Enum


class LDAPUsersUmlautsInUserIds(str, Enum):
    KEEP_UMLAUTS = "keep_umlauts"
    REPLACE_UMLAUTS = "replace_umlauts"

    def __str__(self) -> str:
        return str(self.value)
