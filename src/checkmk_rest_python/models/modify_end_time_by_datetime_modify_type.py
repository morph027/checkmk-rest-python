from enum import Enum


class ModifyEndTimeByDatetimeModifyType(str, Enum):
    ABSOLUTE = "absolute"
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
