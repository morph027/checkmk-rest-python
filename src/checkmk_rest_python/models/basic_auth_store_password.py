from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.basic_auth_store_password_option import BasicAuthStorePasswordOption

T = TypeVar("T", bound="BasicAuthStorePassword")


@_attrs_define
class BasicAuthStorePassword:
    """
    Attributes:
        option (BasicAuthStorePasswordOption):  Example: password_store_id.
        username (str): Your username Example: username_example.
        store_id (str): A password store ID Example: stored_password_1.
    """

    option: BasicAuthStorePasswordOption
    username: str
    store_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        username = self.username

        store_id = self.store_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "username": username,
                "store_id": store_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = BasicAuthStorePasswordOption(d.pop("option"))

        username = d.pop("username")

        store_id = d.pop("store_id")

        basic_auth_store_password = cls(
            option=option,
            username=username,
            store_id=store_id,
        )

        basic_auth_store_password.additional_properties = d
        return basic_auth_store_password

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
