from enum import Enum


class HostUpdateAttributeTagPiggyback(str, Enum):
    AUTO_PIGGYBACK = "auto-piggyback"
    NO_PIGGYBACK = "no-piggyback"
    PIGGYBACK = "piggyback"

    def __str__(self) -> str:
        return str(self.value)
