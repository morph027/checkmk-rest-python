from enum import Enum


class ConcreteUserInterfaceAttributesShowMode(str, Enum):
    DEFAULT = "default"
    DEFAULT_SHOW_LESS = "default_show_less"
    DEFAULT_SHOW_MORE = "default_show_more"
    ENFORCE_SHOW_MORE = "enforce_show_more"

    def __str__(self) -> str:
        return str(self.value)
