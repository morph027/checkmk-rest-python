from enum import Enum


class CreateInFolderOption(str, Enum):
    CREATE_IN_FOLDER = "create_in_folder"
    CREATE_IN_HOST_LOCATION = "create_in_host_location"
    NO_GATEWAY_HOSTS = "no_gateway_hosts"

    def __str__(self) -> str:
        return str(self.value)
