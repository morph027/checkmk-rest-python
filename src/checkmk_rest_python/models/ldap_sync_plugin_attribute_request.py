from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LDAPSyncPluginAttributeRequest")


@_attrs_define
class LDAPSyncPluginAttributeRequest:
    """
    Attributes:
        state (Any): This config parameter is enabled. Default: 'enabled'. Example: enabled.
        attribute_to_sync (str): The attribute to sync
    """

    attribute_to_sync: str
    state: Any = "enabled"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        attribute_to_sync = self.attribute_to_sync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "attribute_to_sync": attribute_to_sync,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state")

        attribute_to_sync = d.pop("attribute_to_sync")

        ldap_sync_plugin_attribute_request = cls(
            state=state,
            attribute_to_sync=attribute_to_sync,
        )

        ldap_sync_plugin_attribute_request.additional_properties = d
        return ldap_sync_plugin_attribute_request

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
