from enum import Enum


class CmkGuiOpenapiEndpointsAuditLogGetAllObjectType(str, Enum):
    ALL = "All"
    FOLDER = "Folder"
    HOST = "Host"
    NONE = "None"
    RULE = "Rule"
    RULESET = "Ruleset"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
