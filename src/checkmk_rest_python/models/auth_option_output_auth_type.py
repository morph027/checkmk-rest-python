from enum import Enum


class AuthOptionOutputAuthType(str, Enum):
    AUTOMATION = "automation"
    LDAP = "ldap"
    PASSWORD = "password"
    SAML2 = "saml2"

    def __str__(self) -> str:
        return str(self.value)
