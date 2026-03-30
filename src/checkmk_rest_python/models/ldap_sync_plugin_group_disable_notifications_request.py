from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ldap_sync_plugin_groups_value_request import (
        LDAPSyncPluginGroupsValueRequest,
    )


T = TypeVar("T", bound="LDAPSyncPluginGroupDisableNotificationsRequest")


@_attrs_define
class LDAPSyncPluginGroupDisableNotificationsRequest:
    """
    Attributes:
        group_cn (str): The common name of the group Example: a_group_cn.
        attribute_to_set (str): The attribute to set Example: disable_notifications.
        value (LDAPSyncPluginGroupsValueRequest):
    """

    group_cn: str
    attribute_to_set: str
    value: LDAPSyncPluginGroupsValueRequest
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_cn = self.group_cn

        attribute_to_set = self.attribute_to_set

        value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_cn": group_cn,
                "attribute_to_set": attribute_to_set,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_sync_plugin_groups_value_request import (
            LDAPSyncPluginGroupsValueRequest,
        )

        d = dict(src_dict)
        group_cn = d.pop("group_cn")

        attribute_to_set = d.pop("attribute_to_set")

        value = LDAPSyncPluginGroupsValueRequest.from_dict(d.pop("value"))

        ldap_sync_plugin_group_disable_notifications_request = cls(
            group_cn=group_cn,
            attribute_to_set=attribute_to_set,
            value=value,
        )

        ldap_sync_plugin_group_disable_notifications_request.additional_properties = d
        return ldap_sync_plugin_group_disable_notifications_request

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
