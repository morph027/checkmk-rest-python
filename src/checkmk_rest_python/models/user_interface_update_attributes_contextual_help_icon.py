from enum import Enum


class UserInterfaceUpdateAttributesContextualHelpIcon(str, Enum):
    HIDE_ICON = "hide_icon"
    SHOW_ICON = "show_icon"

    def __str__(self) -> str:
        return str(self.value)
