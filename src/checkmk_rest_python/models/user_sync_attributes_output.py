from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSyncAttributesOutput")


@_attrs_define
class UserSyncAttributesOutput:
    """
    Attributes:
        sync_with_ldap_connections (str): Sync with ldap connections. The options are ldap, all, disabled. Example:
            ldap.
        ldap_connections (list[str] | Unset): A list of ldap connections. Example: ['LDAP_1', 'LDAP_2'].
    """

    sync_with_ldap_connections: str
    ldap_connections: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_with_ldap_connections = self.sync_with_ldap_connections

        ldap_connections: list[str] | Unset = UNSET
        if not isinstance(self.ldap_connections, Unset):
            ldap_connections = self.ldap_connections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_with_ldap_connections": sync_with_ldap_connections,
            }
        )
        if ldap_connections is not UNSET:
            field_dict["ldap_connections"] = ldap_connections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_with_ldap_connections = d.pop("sync_with_ldap_connections")

        ldap_connections = cast(list[str], d.pop("ldap_connections", UNSET))

        user_sync_attributes_output = cls(
            sync_with_ldap_connections=sync_with_ldap_connections,
            ldap_connections=ldap_connections,
        )

        user_sync_attributes_output.additional_properties = d
        return user_sync_attributes_output

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
