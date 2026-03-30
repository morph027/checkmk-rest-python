from enum import Enum


class HostUpdateAttributeTagNetworking(str, Enum):
    DMZ = "dmz"
    LAN = "lan"
    WAN = "wan"

    def __str__(self) -> str:
        return str(self.value)
