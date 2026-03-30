from enum import Enum


class EditUserRoleNewPermissionsAdditionalProperty(str, Enum):
    DEFAULT = "default"
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
