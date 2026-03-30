from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_from_to_fields import LDAPFromToFields


T = TypeVar("T", bound="LDAPDisableNotificationsValue")


@_attrs_define
class LDAPDisableNotificationsValue:
    """
    Attributes:
        temporarily_disable_all_notifications (bool | Unset): When this option is active you will not get any alerts or
            other notifications via email, SMS or similar. This overrides all other notification settings and rules, so make
            sure that you know what you are doing. Example: True.
        custom_time_range (LDAPFromToFields | Unset):
    """

    temporarily_disable_all_notifications: bool | Unset = UNSET
    custom_time_range: LDAPFromToFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        temporarily_disable_all_notifications = (
            self.temporarily_disable_all_notifications
        )

        custom_time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_time_range, Unset):
            custom_time_range = self.custom_time_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if temporarily_disable_all_notifications is not UNSET:
            field_dict["temporarily_disable_all_notifications"] = (
                temporarily_disable_all_notifications
            )
        if custom_time_range is not UNSET:
            field_dict["custom_time_range"] = custom_time_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_from_to_fields import LDAPFromToFields

        d = dict(src_dict)
        temporarily_disable_all_notifications = d.pop(
            "temporarily_disable_all_notifications", UNSET
        )

        _custom_time_range = d.pop("custom_time_range", UNSET)
        custom_time_range: LDAPFromToFields | Unset
        if isinstance(_custom_time_range, Unset):
            custom_time_range = UNSET
        else:
            custom_time_range = LDAPFromToFields.from_dict(_custom_time_range)

        ldap_disable_notifications_value = cls(
            temporarily_disable_all_notifications=temporarily_disable_all_notifications,
            custom_time_range=custom_time_range,
        )

        ldap_disable_notifications_value.additional_properties = d
        return ldap_disable_notifications_value

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
