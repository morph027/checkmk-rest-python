from enum import Enum


class LDAPGeneralPropertiesUpdateRequestRuleActivation(str, Enum):
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"

    def __str__(self) -> str:
        return str(self.value)
