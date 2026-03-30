from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_update_password_auth_type import AuthUpdatePasswordAuthType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthUpdatePassword")


@_attrs_define
class AuthUpdatePassword:
    """
    Attributes:
        auth_type (AuthUpdatePasswordAuthType): The authentication type Example: password.
        password (str | Unset): The password for login Example: password.
        enforce_password_change (bool | Unset): If set to True, the user will be forced to change his password on the
            next login or access
    """

    auth_type: AuthUpdatePasswordAuthType
    password: str | Unset = UNSET
    enforce_password_change: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type.value

        password = self.password

        enforce_password_change = self.enforce_password_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_type": auth_type,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if enforce_password_change is not UNSET:
            field_dict["enforce_password_change"] = enforce_password_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_type = AuthUpdatePasswordAuthType(d.pop("auth_type"))

        password = d.pop("password", UNSET)

        enforce_password_change = d.pop("enforce_password_change", UNSET)

        auth_update_password = cls(
            auth_type=auth_type,
            password=password,
            enforce_password_change=enforce_password_change,
        )

        auth_update_password.additional_properties = d
        return auth_update_password

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
