from enum import Enum


class EnableSynchronousDeliveryViaSMTPEncryption(str, Enum):
    SSL_TLS = "ssl_tls"
    STARTTLS = "starttls"

    def __str__(self) -> str:
        return str(self.value)
