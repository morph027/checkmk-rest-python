from enum import Enum


class ECEventAttributesServiceLevel(str, Enum):
    GOLD = "gold"
    NO_SERVICE_LEVEL = "no_service_level"
    PLATINUM = "platinum"
    SILVER = "silver"

    def __str__(self) -> str:
        return str(self.value)
