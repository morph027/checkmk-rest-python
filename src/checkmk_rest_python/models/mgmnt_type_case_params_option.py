from enum import Enum


class MgmntTypeCaseParamsOption(str, Enum):
    CASE = "case"
    INCIDENT = "incident"

    def __str__(self) -> str:
        return str(self.value)
