from enum import Enum


class HostUpdateAttributeTagAddressFamily(str, Enum):
    IP_V4V6 = "ip-v4v6"
    IP_V4_ONLY = "ip-v4-only"
    IP_V6_ONLY = "ip-v6-only"
    NO_IP = "no-ip"

    def __str__(self) -> str:
        return str(self.value)
