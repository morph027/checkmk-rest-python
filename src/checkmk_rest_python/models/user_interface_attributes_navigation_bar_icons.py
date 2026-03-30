from enum import Enum


class UserInterfaceAttributesNavigationBarIcons(str, Enum):
    HIDE = "hide"
    SHOW = "show"

    def __str__(self) -> str:
        return str(self.value)
