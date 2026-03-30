from enum import Enum


class CheckboxWithListOfLabelsOutputState(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
