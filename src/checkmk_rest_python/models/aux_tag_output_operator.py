from enum import Enum


class AuxTagOutputOperator(str, Enum):
    IS_NOT_SET = "is_not_set"
    IS_SET = "is_set"

    def __str__(self) -> str:
        return str(self.value)
