from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.smsapi_explicit_password_option import SMSAPIExplicitPasswordOption

T = TypeVar("T", bound="SMSAPIExplicitPassword")


@_attrs_define
class SMSAPIExplicitPassword:
    """
    Attributes:
        option (SMSAPIExplicitPasswordOption):  Example: store.
        password (str):  Example: https://example_webhook_url.com.
    """

    option: SMSAPIExplicitPasswordOption
    password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = SMSAPIExplicitPasswordOption(d.pop("option"))

        password = d.pop("password")

        smsapi_explicit_password = cls(
            option=option,
            password=password,
        )

        smsapi_explicit_password.additional_properties = d
        return smsapi_explicit_password

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
