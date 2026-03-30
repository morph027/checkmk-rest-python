from enum import Enum


class LabelCondition1Operator(str, Enum):
    AND = "and"
    NOT = "not"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
