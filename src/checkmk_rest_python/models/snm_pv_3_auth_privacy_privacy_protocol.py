from enum import Enum


class SNMPv3AuthPrivacyPrivacyProtocol(str, Enum):
    AES_128 = "AES-128"
    AES_192 = "AES-192"
    AES_192_BLUMENTHAL = "AES-192-Blumenthal"
    AES_256 = "AES-256"
    AES_256_BLUMENTHAL = "AES-256-Blumenthal"
    CBC_DES = "CBC-DES"
    VALUE_2 = "3DES-EDE"

    def __str__(self) -> str:
        return str(self.value)
