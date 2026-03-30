from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_disable_notifications_value import LDAPDisableNotificationsValue


T = TypeVar("T", bound="LDAPGroupsToSyncDisableNotifications")


@_attrs_define
class LDAPGroupsToSyncDisableNotifications:
    """
    Attributes:
        group_cn (str | Unset): The common name of the group in LDAP. This is the name of the group as it is stored in
            the LDAP directory. Example: group_cn_example.
        attribute_to_set (str | Unset): The name of the attribute to set.
        value (LDAPDisableNotificationsValue | Unset):
    """

    group_cn: str | Unset = UNSET
    attribute_to_set: str | Unset = UNSET
    value: LDAPDisableNotificationsValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_cn = self.group_cn

        attribute_to_set = self.attribute_to_set

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_cn is not UNSET:
            field_dict["group_cn"] = group_cn
        if attribute_to_set is not UNSET:
            field_dict["attribute_to_set"] = attribute_to_set
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_disable_notifications_value import (
            LDAPDisableNotificationsValue,
        )

        d = dict(src_dict)
        group_cn = d.pop("group_cn", UNSET)

        attribute_to_set = d.pop("attribute_to_set", UNSET)

        _value = d.pop("value", UNSET)
        value: LDAPDisableNotificationsValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = LDAPDisableNotificationsValue.from_dict(_value)

        ldap_groups_to_sync_disable_notifications = cls(
            group_cn=group_cn,
            attribute_to_set=attribute_to_set,
            value=value,
        )

        ldap_groups_to_sync_disable_notifications.additional_properties = d
        return ldap_groups_to_sync_disable_notifications

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
