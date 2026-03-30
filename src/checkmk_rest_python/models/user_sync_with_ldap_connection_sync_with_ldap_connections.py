from enum import Enum


class UserSyncWithLdapConnectionSyncWithLdapConnections(str, Enum):
    ALL = "all"
    DISABLED = "disabled"
    LDAP = "ldap"

    def __str__(self) -> str:
        return str(self.value)
