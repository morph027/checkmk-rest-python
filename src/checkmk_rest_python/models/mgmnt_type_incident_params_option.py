from enum import Enum


class MgmntTypeIncidentParamsOption(str, Enum):
    CASE = "case"
    INCIDENT = "incident"

    def __str__(self) -> str:
        return str(self.value)
