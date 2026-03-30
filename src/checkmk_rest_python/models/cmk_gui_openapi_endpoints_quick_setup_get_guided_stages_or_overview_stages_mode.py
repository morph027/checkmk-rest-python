from enum import Enum


class CmkGuiOpenapiEndpointsQuickSetupGetGuidedStagesOrOverviewStagesMode(str, Enum):
    GUIDED = "guided"
    OVERVIEW = "overview"

    def __str__(self) -> str:
        return str(self.value)
