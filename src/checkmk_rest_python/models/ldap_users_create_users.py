from enum import Enum


class LDAPUsersCreateUsers(str, Enum):
    ON_LOGIN = "on_login"
    ON_SYNC = "on_sync"

    def __str__(self) -> str:
        return str(self.value)
