from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPSyncPluginNestedOtherConnectionsRequest")


@_attrs_define
class LDAPSyncPluginNestedOtherConnectionsRequest:
    """
    Attributes:
        state (Any): This config parameter is enabled. Default: 'enabled'. Example: enabled.
        handle_nested (bool | Unset): Once you enable this option, this plug-in will not only handle direct group
            memberships, instead it will also dig into nested groups and treat the members of those groups as contact group
            members as well. Please bear in mind that this feature might increase the execution time of your LDAP sync.
            Default: False. Example: True.
        sync_from_other_connections (list[str] | Unset): The LDAP attribute whose contents shall be synced into this
            custom attribute. Example: ['LDAP_1', 'LDAP_2'].
    """

    state: Any = "enabled"
    handle_nested: bool | Unset = False
    sync_from_other_connections: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        handle_nested = self.handle_nested

        sync_from_other_connections: list[str] | Unset = UNSET
        if not isinstance(self.sync_from_other_connections, Unset):
            sync_from_other_connections = self.sync_from_other_connections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if handle_nested is not UNSET:
            field_dict["handle_nested"] = handle_nested
        if sync_from_other_connections is not UNSET:
            field_dict["sync_from_other_connections"] = sync_from_other_connections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state")

        handle_nested = d.pop("handle_nested", UNSET)

        sync_from_other_connections = cast(
            list[str], d.pop("sync_from_other_connections", UNSET)
        )

        ldap_sync_plugin_nested_other_connections_request = cls(
            state=state,
            handle_nested=handle_nested,
            sync_from_other_connections=sync_from_other_connections,
        )

        ldap_sync_plugin_nested_other_connections_request.additional_properties = d
        return ldap_sync_plugin_nested_other_connections_request

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
