from enum import Enum


class FolderUpdateAttributeTagSnmpDs(str, Enum):
    NO_SNMP = "no-snmp"
    SNMP_V1 = "snmp-v1"
    SNMP_V2 = "snmp-v2"

    def __str__(self) -> str:
        return str(self.value)
