from enum import Enum


class SMSAPIPluginCreateModemType(str, Enum):
    TRB140 = "trb140"

    def __str__(self) -> str:
        return str(self.value)
