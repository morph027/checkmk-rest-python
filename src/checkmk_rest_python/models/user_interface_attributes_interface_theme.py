from enum import Enum


class UserInterfaceAttributesInterfaceTheme(str, Enum):
    DARK = "dark"
    DEFAULT = "default"
    LIGHT = "light"

    def __str__(self) -> str:
        return str(self.value)
