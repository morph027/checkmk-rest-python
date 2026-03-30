from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_sync_plugin_alias_state import LDAPSyncPluginAliasState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPSyncPluginAlias")


@_attrs_define
class LDAPSyncPluginAlias:
    """
    Attributes:
        state (LDAPSyncPluginAliasState | Unset):  Example: enabled.
        attribute_to_sync (str | Unset): The LDAP attribute containing the alias of the user.
    """

    state: LDAPSyncPluginAliasState | Unset = UNSET
    attribute_to_sync: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        attribute_to_sync = self.attribute_to_sync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if attribute_to_sync is not UNSET:
            field_dict["attribute_to_sync"] = attribute_to_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPSyncPluginAliasState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPSyncPluginAliasState(_state)

        attribute_to_sync = d.pop("attribute_to_sync", UNSET)

        ldap_sync_plugin_alias = cls(
            state=state,
            attribute_to_sync=attribute_to_sync,
        )

        ldap_sync_plugin_alias.additional_properties = d
        return ldap_sync_plugin_alias

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
