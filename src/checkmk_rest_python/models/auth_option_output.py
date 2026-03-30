from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_option_output_auth_type import AuthOptionOutputAuthType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthOptionOutput")


@_attrs_define
class AuthOptionOutput:
    """
    Attributes:
        auth_type (AuthOptionOutputAuthType | Unset):  Example: password.
        store_automation_secret (bool | Unset): If set to True, the secret is stored
        enforce_password_change (bool | Unset): If set to True, the user will be forced to change his password on the
            next login or access. Defaults to False
    """

    auth_type: AuthOptionOutputAuthType | Unset = UNSET
    store_automation_secret: bool | Unset = UNSET
    enforce_password_change: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        store_automation_secret = self.store_automation_secret

        enforce_password_change = self.enforce_password_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if store_automation_secret is not UNSET:
            field_dict["store_automation_secret"] = store_automation_secret
        if enforce_password_change is not UNSET:
            field_dict["enforce_password_change"] = enforce_password_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auth_type = d.pop("auth_type", UNSET)
        auth_type: AuthOptionOutputAuthType | Unset
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = AuthOptionOutputAuthType(_auth_type)

        store_automation_secret = d.pop("store_automation_secret", UNSET)

        enforce_password_change = d.pop("enforce_password_change", UNSET)

        auth_option_output = cls(
            auth_type=auth_type,
            store_automation_secret=store_automation_secret,
            enforce_password_change=enforce_password_change,
        )

        auth_option_output.additional_properties = d
        return auth_option_output

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
