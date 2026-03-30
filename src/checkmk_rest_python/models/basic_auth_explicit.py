from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.basic_auth_explicit_option import BasicAuthExplicitOption

T = TypeVar("T", bound="BasicAuthExplicit")


@_attrs_define
class BasicAuthExplicit:
    """
    Attributes:
        option (BasicAuthExplicitOption):  Example: password_store_id.
        username (str): Your username Example: username_example.
        password (str): Your password Example: password_example.
    """

    option: BasicAuthExplicitOption
    username: str
    password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "username": username,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = BasicAuthExplicitOption(d.pop("option"))

        username = d.pop("username")

        password = d.pop("password")

        basic_auth_explicit = cls(
            option=option,
            username=username,
            password=password,
        )

        basic_auth_explicit.additional_properties = d
        return basic_auth_explicit

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
