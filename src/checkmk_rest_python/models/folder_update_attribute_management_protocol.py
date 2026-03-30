from enum import Enum


class FolderUpdateAttributeManagementProtocol(str, Enum):
    IPMI = "ipmi"
    NONE = "none"
    SNMP = "snmp"

    def __str__(self) -> str:
        return str(self.value)
