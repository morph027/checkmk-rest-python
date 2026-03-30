from enum import Enum


class HostOrServiceConditionOperator(str, Enum):
    NONE_OF = "none_of"
    ONE_OF = "one_of"

    def __str__(self) -> str:
        return str(self.value)
