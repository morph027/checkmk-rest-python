from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_sync_with_ldap_connection_sync_with_ldap_connections import (
    UserSyncWithLdapConnectionSyncWithLdapConnections,
)

T = TypeVar("T", bound="UserSyncWithLdapConnection")


@_attrs_define
class UserSyncWithLdapConnection:
    """
    Attributes:
        sync_with_ldap_connections (UserSyncWithLdapConnectionSyncWithLdapConnections): Sync with ldap connections. The
            options are ldap, all, disabled. Example: ldap.
        ldap_connections (list[str]): A list of ldap connections. Example: ['LDAP_1', 'LDAP_2'].
    """

    sync_with_ldap_connections: UserSyncWithLdapConnectionSyncWithLdapConnections
    ldap_connections: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_with_ldap_connections = self.sync_with_ldap_connections.value

        ldap_connections = self.ldap_connections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_with_ldap_connections": sync_with_ldap_connections,
                "ldap_connections": ldap_connections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_with_ldap_connections = UserSyncWithLdapConnectionSyncWithLdapConnections(
            d.pop("sync_with_ldap_connections")
        )

        ldap_connections = cast(list[str], d.pop("ldap_connections"))

        user_sync_with_ldap_connection = cls(
            sync_with_ldap_connections=sync_with_ldap_connections,
            ldap_connections=ldap_connections,
        )

        user_sync_with_ldap_connection.additional_properties = d
        return user_sync_with_ldap_connection

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
