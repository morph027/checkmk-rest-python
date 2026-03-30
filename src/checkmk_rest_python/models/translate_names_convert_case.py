from enum import Enum


class TranslateNamesConvertCase(str, Enum):
    LOWER = "lower"
    NOP = "nop"
    UPPER = "upper"

    def __str__(self) -> str:
        return str(self.value)
