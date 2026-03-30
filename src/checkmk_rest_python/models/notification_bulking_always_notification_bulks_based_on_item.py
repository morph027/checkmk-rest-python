from enum import Enum


class NotificationBulkingAlwaysNotificationBulksBasedOnItem(str, Enum):
    CHECK_TYPE = "check_type"
    EC_COMMENT = "ec_comment"
    EC_CONTACT = "ec_contact"
    FOLDER = "folder"
    HOST = "host"
    SERVICE = "service"
    SL = "sl"
    STATE = "state"

    def __str__(self) -> str:
        return str(self.value)
