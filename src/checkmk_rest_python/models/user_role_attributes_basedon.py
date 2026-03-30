from enum import Enum


class UserRoleAttributesBasedon(str, Enum):
    ADMIN = "admin"
    AGENT_REGISTRATION = "agent_registration"
    GUEST = "guest"
    NO_PERMISSIONS = "no_permissions"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
