from enum import Enum


class UserIdleOptionOption(str, Enum):
    DISABLE = "disable"
    GLOBAL = "global"
    INDIVIDUAL = "individual"

    def __str__(self) -> str:
        return str(self.value)
