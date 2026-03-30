from enum import Enum


class SlackWebhookStoreOption(str, Enum):
    EXPLICIT = "explicit"
    STORE = "store"

    def __str__(self) -> str:
        return str(self.value)
