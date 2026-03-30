from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_connection import LDAPConnection
    from ..models.ldap_general_properties import LDAPGeneralProperties
    from ..models.ldap_groups import LDAPGroups
    from ..models.ldap_other import LDAPOther
    from ..models.ldap_sync_plugins_with_custom_attributes import (
        LDAPSyncPluginsWithCustomAttributes,
    )
    from ..models.ldap_users import LDAPUsers


T = TypeVar("T", bound="LDAPConnectionConfig")


@_attrs_define
class LDAPConnectionConfig:
    """
    Attributes:
        general_properties (LDAPGeneralProperties | Unset):
        ldap_connection (LDAPConnection | Unset):
        users (LDAPUsers | Unset):
        groups (LDAPGroups | Unset):
        sync_plugins (LDAPSyncPluginsWithCustomAttributes | Unset):
        other (LDAPOther | Unset):
    """

    general_properties: LDAPGeneralProperties | Unset = UNSET
    ldap_connection: LDAPConnection | Unset = UNSET
    users: LDAPUsers | Unset = UNSET
    groups: LDAPGroups | Unset = UNSET
    sync_plugins: LDAPSyncPluginsWithCustomAttributes | Unset = UNSET
    other: LDAPOther | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        general_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.general_properties, Unset):
            general_properties = self.general_properties.to_dict()

        ldap_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap_connection, Unset):
            ldap_connection = self.ldap_connection.to_dict()

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        sync_plugins: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sync_plugins, Unset):
            sync_plugins = self.sync_plugins.to_dict()

        other: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if general_properties is not UNSET:
            field_dict["general_properties"] = general_properties
        if ldap_connection is not UNSET:
            field_dict["ldap_connection"] = ldap_connection
        if users is not UNSET:
            field_dict["users"] = users
        if groups is not UNSET:
            field_dict["groups"] = groups
        if sync_plugins is not UNSET:
            field_dict["sync_plugins"] = sync_plugins
        if other is not UNSET:
            field_dict["other"] = other

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_connection import LDAPConnection
        from ..models.ldap_general_properties import LDAPGeneralProperties
        from ..models.ldap_groups import LDAPGroups
        from ..models.ldap_other import LDAPOther
        from ..models.ldap_sync_plugins_with_custom_attributes import (
            LDAPSyncPluginsWithCustomAttributes,
        )
        from ..models.ldap_users import LDAPUsers

        d = dict(src_dict)
        _general_properties = d.pop("general_properties", UNSET)
        general_properties: LDAPGeneralProperties | Unset
        if isinstance(_general_properties, Unset):
            general_properties = UNSET
        else:
            general_properties = LDAPGeneralProperties.from_dict(_general_properties)

        _ldap_connection = d.pop("ldap_connection", UNSET)
        ldap_connection: LDAPConnection | Unset
        if isinstance(_ldap_connection, Unset):
            ldap_connection = UNSET
        else:
            ldap_connection = LDAPConnection.from_dict(_ldap_connection)

        _users = d.pop("users", UNSET)
        users: LDAPUsers | Unset
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = LDAPUsers.from_dict(_users)

        _groups = d.pop("groups", UNSET)
        groups: LDAPGroups | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = LDAPGroups.from_dict(_groups)

        _sync_plugins = d.pop("sync_plugins", UNSET)
        sync_plugins: LDAPSyncPluginsWithCustomAttributes | Unset
        if isinstance(_sync_plugins, Unset):
            sync_plugins = UNSET
        else:
            sync_plugins = LDAPSyncPluginsWithCustomAttributes.from_dict(_sync_plugins)

        _other = d.pop("other", UNSET)
        other: LDAPOther | Unset
        if isinstance(_other, Unset):
            other = UNSET
        else:
            other = LDAPOther.from_dict(_other)

        ldap_connection_config = cls(
            general_properties=general_properties,
            ldap_connection=ldap_connection,
            users=users,
            groups=groups,
            sync_plugins=sync_plugins,
            other=other,
        )

        ldap_connection_config.additional_properties = d
        return ldap_connection_config

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
