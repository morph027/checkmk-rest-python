from enum import Enum


class UpdateConfigurationEntityEntityType(str, Enum):
    FOLDER = "folder"
    NOTIFICATION_PARAMETER = "notification_parameter"
    PASSWORDSTORE_PASSWORD = "passwordstore_password"

    def __str__(self) -> str:
        return str(self.value)
