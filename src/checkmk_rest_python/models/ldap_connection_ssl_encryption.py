from enum import Enum


class LDAPConnectionSslEncryption(str, Enum):
    DISABLE_SSL = "disable_ssl"
    ENABLE_SSL = "enable_ssl"

    def __str__(self) -> str:
        return str(self.value)
