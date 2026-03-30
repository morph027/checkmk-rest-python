from enum import Enum


class LDAPGeneralPropertiesCreateRequestRuleActivation(str, Enum):
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"

    def __str__(self) -> str:
        return str(self.value)
