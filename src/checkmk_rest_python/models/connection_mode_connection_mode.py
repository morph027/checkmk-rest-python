from enum import Enum


class ConnectionModeConnectionMode(str, Enum):
    PULL_AGENT = "pull-agent"
    PUSH_AGENT = "push-agent"

    def __str__(self) -> str:
        return str(self.value)
