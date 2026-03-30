from enum import Enum


class UserDismissWarningWarning(str, Enum):
    IMMEDIATE_SLIDEOUT_CHANGE = "immediate_slideout_change"
    NOTIFICATION_FALLBACK = "notification_fallback"

    def __str__(self) -> str:
        return str(self.value)
