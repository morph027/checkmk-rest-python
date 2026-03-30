from enum import Enum


class UserInterfaceUpdateAttributesNavigationBarIcons(str, Enum):
    HIDE = "hide"
    SHOW = "show"

    def __str__(self) -> str:
        return str(self.value)
