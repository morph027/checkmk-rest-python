from enum import Enum


class FolderUpdateAttributeTagNetworking(str, Enum):
    DMZ = "dmz"
    LAN = "lan"
    WAN = "wan"

    def __str__(self) -> str:
        return str(self.value)
