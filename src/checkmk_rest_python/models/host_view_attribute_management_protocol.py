from enum import Enum


class HostViewAttributeManagementProtocol(str, Enum):
    IPMI = "ipmi"
    NONE = "none"
    SNMP = "snmp"

    def __str__(self) -> str:
        return str(self.value)
