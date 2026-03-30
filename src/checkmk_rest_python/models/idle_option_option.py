from enum import Enum


class IdleOptionOption(str, Enum):
    DISABLE = "disable"
    GLOBAL = "global"
    INDIVIDUAL = "individual"

    def __str__(self) -> str:
        return str(self.value)
