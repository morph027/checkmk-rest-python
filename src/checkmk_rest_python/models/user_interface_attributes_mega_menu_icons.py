from enum import Enum


class UserInterfaceAttributesMegaMenuIcons(str, Enum):
    ENTRY = "entry"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
