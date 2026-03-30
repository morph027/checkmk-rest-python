from enum import Enum


class SNMPv3AuthNoPrivacyAuthProtocol(str, Enum):
    MD5_96 = "MD5-96"
    SHA_1_96 = "SHA-1-96"
    SHA_2_224 = "SHA-2-224"
    SHA_2_256 = "SHA-2-256"
    SHA_2_384 = "SHA-2-384"
    SHA_2_512 = "SHA-2-512"

    def __str__(self) -> str:
        return str(self.value)
