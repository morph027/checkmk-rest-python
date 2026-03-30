from enum import Enum


class CheckBoxUseSiteIDPrefixValue(str, Enum):
    DEACTIVATED = "deactivated"
    USE_SITE_ID = "use_site_id"

    def __str__(self) -> str:
        return str(self.value)
