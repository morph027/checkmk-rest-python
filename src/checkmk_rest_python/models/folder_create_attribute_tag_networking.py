from enum import Enum


class FolderCreateAttributeTagNetworking(str, Enum):
    DMZ = "dmz"
    LAN = "lan"
    WAN = "wan"

    def __str__(self) -> str:
        return str(self.value)
