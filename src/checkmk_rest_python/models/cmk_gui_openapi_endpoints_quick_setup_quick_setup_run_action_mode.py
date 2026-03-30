from enum import Enum


class CmkGuiOpenapiEndpointsQuickSetupQuickSetupRunActionMode(str, Enum):
    GUIDED = "guided"
    OVERVIEW = "overview"

    def __str__(self) -> str:
        return str(self.value)
