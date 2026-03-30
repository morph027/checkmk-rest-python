from enum import Enum


class CheckboxWithListOfEmailInfoStrsState(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
