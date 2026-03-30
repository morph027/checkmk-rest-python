from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_update_remove_auth_type import AuthUpdateRemoveAuthType

T = TypeVar("T", bound="AuthUpdateRemove")


@_attrs_define
class AuthUpdateRemove:
    """
    Attributes:
        auth_type (AuthUpdateRemoveAuthType): The authentication type Example: password.
    """

    auth_type: AuthUpdateRemoveAuthType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_type": auth_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_type = AuthUpdateRemoveAuthType(d.pop("auth_type"))

        auth_update_remove = cls(
            auth_type=auth_type,
        )

        auth_update_remove.additional_properties = d
        return auth_update_remove

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
