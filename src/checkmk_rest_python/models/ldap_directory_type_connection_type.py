from enum import Enum


class LDAPDirectoryTypeConnectionType(str, Enum):
    ACTIVE_DIRECTORY_AUTOMATIC = "active_directory_automatic"
    ACTIVE_DIRECTORY_MANUAL = "active_directory_manual"
    OPEN_LDAP = "open_ldap"
    VALUE_3 = "389_directory_server"

    def __str__(self) -> str:
        return str(self.value)
