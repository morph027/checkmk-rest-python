from enum import Enum


class CheckboxWithStrValueOutputState(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
