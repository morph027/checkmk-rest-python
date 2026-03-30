from enum import Enum


class HostCreateAttributeTagCriticality(str, Enum):
    CRITICAL = "critical"
    OFFLINE = "offline"
    PROD = "prod"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
