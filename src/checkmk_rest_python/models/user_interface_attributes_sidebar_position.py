from enum import Enum


class UserInterfaceAttributesSidebarPosition(str, Enum):
    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return str(self.value)
