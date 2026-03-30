from enum import Enum


class EventConsoleAlertAttributesMatchType(str, Enum):
    DO_NOT_MATCH_EVENT_CONSOLE_ALERTS = "do_not_match_event_console_alerts"
    MATCH_ONLY_EVENT_CONSOLE_ALERTS = "match_only_event_console_alerts"

    def __str__(self) -> str:
        return str(self.value)
