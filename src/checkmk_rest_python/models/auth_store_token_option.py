from enum import Enum


class AuthStoreTokenOption(str, Enum):
    EXPLICIT_PASSWORD = "explicit_password"
    EXPLICIT_TOKEN = "explicit_token"
    PASSWORD_STORE_ID = "password_store_id"
    TOKEN_STORE_ID = "token_store_id"

    def __str__(self) -> str:
        return str(self.value)
