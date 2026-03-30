from enum import Enum


class PluginBaseOption(str, Enum):
    CANCEL_PREVIOUS_NOTIFICATIONS = "cancel_previous_notifications"
    CREATE_NOTIFICATION_WITH_CUSTOM_PARAMETERS = (
        "create_notification_with_custom_parameters"
    )
    CREATE_NOTIFICATION_WITH_THE_FOLLOWING_PARAMETERS = (
        "create_notification_with_the_following_parameters"
    )

    def __str__(self) -> str:
        return str(self.value)
