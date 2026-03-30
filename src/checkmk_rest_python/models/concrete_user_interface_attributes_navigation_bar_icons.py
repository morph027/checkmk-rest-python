from enum import Enum


class ConcreteUserInterfaceAttributesNavigationBarIcons(str, Enum):
    HIDE = "hide"
    SHOW = "show"

    def __str__(self) -> str:
        return str(self.value)
