from enum import Enum


class ActivationSiteStatusState(str, Enum):
    ERROR = "error"
    SUCCESS = "success"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
