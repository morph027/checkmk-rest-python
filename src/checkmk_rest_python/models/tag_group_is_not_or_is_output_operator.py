from enum import Enum


class TagGroupIsNotOrIsOutputOperator(str, Enum):
    IS = "is"
    IS_NOT = "is_not"

    def __str__(self) -> str:
        return str(self.value)
